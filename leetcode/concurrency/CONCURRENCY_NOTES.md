# Python Concurrency Primitives — Study Notes

> Based on LeetCode 1114: Print in Order

---

## Table of Contents
1. [The Problem](#the-problem)
2. [Solution 1: Busy-Wait (Flag)](#solution-1-busy-wait-flag)
3. [Solution 2: Lock](#solution-2-lock)
4. [Solution 3: Semaphore](#solution-3-semaphore)
5. [Solution 4: Barrier](#solution-4-barrier)
6. [Lock vs Semaphore — Deep Comparison](#lock-vs-semaphore--deep-comparison)
7. [When to Use Which](#when-to-use-which)
8. [Semaphore Use Cases](#semaphore-use-cases)
9. [References](#references)

---

## The Problem

Three methods `first()`, `second()`, `third()` are called concurrently by three threads.
They **must always execute in order**: first → second → third, regardless of thread scheduling.

---

## Solution 1: Busy-Wait (Flag)

```python
class Foo:
    def __init__(self):
        self.first_done = False
        self.second_done = False

    def first(self, printFirst):
        printFirst()
        self.first_done = True

    def second(self, printSecond):
        while not self.first_done:  # spin loop
            continue
        printSecond()
        self.second_done = True

    def third(self, printThird):
        while not self.second_done:  # spin loop
            continue
        printThird()
```

**How it works:** `second` and `third` continuously poll a boolean flag.

| Pros | Cons |
|---|---|
| Simple to understand | 🔴 Burns 100% CPU spinning |
| No imports needed | Not thread-safe on all platforms (no memory barrier) |
| | Wastes energy / starves other threads |

---

## Solution 2: Lock

```python
class FooLock:
    def __init__(self):
        self.lock1 = threading.Lock()
        self.lock1.acquire()   # pre-lock: second() will block on acquire()

        self.lock2 = threading.Lock()
        self.lock2.acquire()   # pre-lock: third() will block on acquire()

    def first(self, printFirst):
        printFirst()
        self.lock1.release()   # unblocks second()

    def second(self, printSecond):
        self.lock1.acquire()   # blocks until first() releases
        printSecond()
        self.lock2.release()   # unblocks third()

    def third(self, printThird):
        self.lock2.acquire()   # blocks until second() releases
        printThird()
```

**How it works:** Both locks are acquired in `__init__` (main thread).
Worker threads block trying to `acquire()` them. The previous method `release()`s to unblock the next.

**The ownership caveat:**
> A `threading.Lock` has **no thread ownership tracking** in CPython — the thread that `acquire()`s it does NOT have to be the one that `release()`s it. This is why it works here, but it is **semantically misusing** a Lock (which is designed for mutual exclusion, not signaling).
>
> If you used `threading.RLock` instead, this would **deadlock** — because `RLock` *does* enforce ownership.

---

## Solution 3: Semaphore ✅ Best for this problem

```python
class FooSemaphore:
    def __init__(self):
        self.sem1 = threading.Semaphore(0)  # counter = 0
        self.sem2 = threading.Semaphore(0)  # counter = 0

    def first(self, printFirst):
        printFirst()
        self.sem1.release()    # counter: 0 → 1, wakes second()

    def second(self, printSecond):
        self.sem1.acquire()    # blocks until counter > 0
        printSecond()
        self.sem2.release()    # counter: 0 → 1, wakes third()

    def third(self, printThird):
        self.sem2.acquire()    # blocks until counter > 0
        printThird()
```

**How it works:** A Semaphore holds an **integer counter**.
- `acquire()` → decrements counter; if it would go below `0`, the thread **blocks**
- `release()` → increments counter, **wakes** one blocked thread

Starting at `0` means any `acquire()` blocks immediately — the perfect signaling primitive.

---

## Solution 4: Barrier

```python
class FooBarrier:
    def __init__(self):
        self.barrier1 = threading.Barrier(2)  # 2 parties must meet
        self.barrier2 = threading.Barrier(2)

    def first(self, printFirst):
        printFirst()
        self.barrier1.wait()   # waits for second() to also arrive

    def second(self, printSecond):
        self.barrier1.wait()   # blocks until first() arrives → both released
        printSecond()
        self.barrier2.wait()   # waits for third() to also arrive

    def third(self, printThird):
        self.barrier2.wait()   # blocks until second() arrives → both released
        printThird()
```

**How it works:** A Barrier blocks all threads until **N parties** have called `.wait()`.
Once all N arrive, **all are released simultaneously**. It is a mutual rendezvous, not a one-way signal.

---

## Lock vs Semaphore — Deep Comparison

### What is a Lock (Mutex)?

A binary switch with exactly **two states**: LOCKED / UNLOCKED.

```
Thread A: lock.acquire()  → owns the lock, others block
Thread A: lock.release()  → releases ownership, one waiter unblocked
```

🔑 **Mental model:** A bathroom with one key — one person holds it, everyone else waits.

**Key property — Ownership:** The thread that acquires a lock *should* be the one to release it.
(Enforced strictly by `RLock`, loosely by `Lock` in CPython.)

---

### What is a Semaphore?

A **counter** (integer ≥ 0) with two atomic operations:

```
acquire()  →  counter -= 1   (blocks if counter would go below 0)
release()  →  counter += 1   (wakes one blocked thread if any)
```

🅿️ **Mental model:** A parking lot with N spots — N cars can park. The (N+1)th waits until one leaves.

**Key property — No Ownership:** *Any* thread can call `release()`, even one that never called `acquire()`.
This is what makes it ideal for **signaling** between different threads.

---

### Side-by-Side

| Property | `threading.Lock` | `threading.Semaphore` |
|---|---|---|
| Internal state | Binary (locked / unlocked) | Integer counter (0 to N) |
| Ownership | Yes (conceptually) | **No** |
| Purpose | **Mutual exclusion** — protect shared data | **Signaling / coordination** between threads |
| Initial value | Unlocked | Any N ≥ 0 |
| `acquire()` blocks when | Already locked | Counter = 0 |
| `release()` must be called by | Same thread (conceptually) | **Any** thread |
| `Semaphore(1)` ≈ `Lock`? | — | Almost, but still no ownership |

---

### Why Semaphore is Better for This Problem

This problem has **no shared resource to protect** — there's nothing to lock.
It's purely about **ordering**: "thread A must finish before thread B starts."

That's the definition of **signaling**, which is exactly what a Semaphore is designed for.

```
Lock:       "Only one thread at a time may enter this region"  → mutual exclusion
Semaphore:  "Thread B may proceed only after Thread A signals" → signaling / ordering
```

Using a Lock here works in CPython but **misuses the abstraction** — it relies on the
implementation detail that CPython's `Lock` doesn't check ownership, which is not guaranteed
and would break with `RLock`.

---

## When to Use Which

| Scenario | Use |
|---|---|
| Protect shared data (e.g., increment a counter) | `Lock` or `RLock` |
| One thread signals another that work is done | `Semaphore(0)` |
| Limit N concurrent accesses to a resource | `Semaphore(N)` |
| Two threads must meet before either proceeds | `Barrier(2)` |
| N threads must all reach a checkpoint together | `Barrier(N)` |
| Ordered pipeline (A → B → C) | `Semaphore(0)` × 2 |
| Prevent more than N threads in a section | `Semaphore(N)` |

---

## Semaphore Use Cases

### 1. Ordered Signaling (this problem)
```python
sem = Semaphore(0)
# Thread A: do_work(); sem.release()
# Thread B: sem.acquire(); do_next_work()
```

### 2. Resource Pool / Connection Limiting
```python
pool = Semaphore(3)   # max 3 DB connections at once
with pool:
    conn = get_connection()
    conn.query(...)
```

### 3. Producer-Consumer
```python
empty = Semaphore(BUFFER_SIZE)  # available slots
filled = Semaphore(0)           # filled slots

# Producer: empty.acquire() → add item → filled.release()
# Consumer: filled.acquire() → take item → empty.release()
```

### 4. Rate Limiting
```python
rate = Semaphore(5)   # max 5 concurrent API requests
with rate:
    requests.get(url)
```

### 5. Readers-Writers
```python
# Many readers simultaneously, but exclusive writer access
write_lock = Semaphore(1)
# First reader acquires write_lock; last reader releases it
# Writer: write_lock.acquire() ... write_lock.release()
```

### 6. Dining Philosophers (Deadlock Prevention)
```python
room = Semaphore(N - 1)  # at most N-1 philosophers "in the room"
# Prevents the circular deadlock where everyone holds one fork
```

---

## References

- 📖 **Python Docs — `threading` module**
  https://docs.python.org/3/library/threading.html

- 📖 **`threading.Semaphore`**
  https://docs.python.org/3/library/threading.html#threading.Semaphore

- 📖 **`threading.Lock`**
  https://docs.python.org/3/library/threading.html#threading.Lock

- 📖 **`threading.Barrier`**
  https://docs.python.org/3/library/threading.html#threading.Barrier

- 🧩 **LeetCode 1114 — Print in Order**
  https://leetcode.com/problems/print-in-order/

- 📚 **"The Little Book of Semaphores" — Allen Downey** (free PDF)
  https://greenteapress.com/wp/semaphores/
  > The definitive resource for learning semaphore patterns (producer-consumer, dining philosophers, readers-writers, barriers, etc.)

- 📚 **"Operating Systems: Three Easy Pieces" — Arpaci-Dusseau** (free online)
  https://pages.cs.wisc.edu/~remzi/OSTEP/
  > Chapters 26–31 cover locks, semaphores, condition variables in depth

- 🐍 **CPython source — `_thread` module (Lock implementation)**
  https://github.com/python/cpython/blob/main/Modules/_threadmodule.c
