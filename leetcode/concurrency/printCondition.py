class Foo:
    def __init__(self):
        self.first_done = False
        self.second_done = False

    def first(self, printFirst: "Callable[[], None]") -> None:

        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.first_done = True

    def second(self, printSecond: "Callable[[], None]") -> None:

        while not self.first_done:
            continue
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.second_done = True

    def third(self, printThird: "Callable[[], None]") -> None:
        while not self.second_done:
            continue
        # printThird() outputs "third". Do not change or remove this line.
        printThird()


import threading


class FooBarrier:
    def __init__(self):
        # barrier1 coordinates first() and second():
        #   - first()  arrives AFTER  printing "first"
        #   - second() arrives BEFORE printing "second"
        # Both must reach barrier1.wait() before either thread continues.
        self.barrier1 = threading.Barrier(2)

        # barrier2 coordinates second() and third():
        #   - second() arrives AFTER  printing "second"
        #   - third()  arrives BEFORE printing "third"
        self.barrier2 = threading.Barrier(2)

    def first(self, printFirst: "Callable[[], None]") -> None:
        # Step 1: No prerequisite — run freely and print "first".
        printFirst()

        # Step 2: Arrive at barrier1 to signal "first is done".
        #         second() is blocked at barrier1.wait() too.
        #         The barrier releases BOTH threads once both have arrived.
        self.barrier1.wait()

    def second(self, printSecond: "Callable[[], None]") -> None:
        # Step 1: Block here until first() also calls barrier1.wait().
        #         Once both parties arrive, the barrier opens and this
        #         thread continues — guaranteeing "first" was printed.
        self.barrier1.wait()

        # Step 2: Safe to print "second" now.
        printSecond()

        # Step 3: Arrive at barrier2 to signal "second is done".
        #         third() is blocked at barrier2.wait() too.
        #         The barrier releases BOTH threads once both have arrived.
        self.barrier2.wait()

    def third(self, printThird: "Callable[[], None]") -> None:
        # Step 1: Block here until second() also calls barrier2.wait().
        #         Once both parties arrive, the barrier opens and this
        #         thread continues — guaranteeing "second" was printed.
        self.barrier2.wait()

        # Step 2: Safe to print "third" now.
        printThird()


class FooLock:
    def __init__(self):
        # lock1 starts LOCKED. second() will block trying to acquire it.
        # first() will release it after printing, unblocking second().
        self.lock1 = threading.Lock()
        self.lock1.acquire()

        # lock2 starts LOCKED. third() will block trying to acquire it.
        # second() will release it after printing, unblocking third().
        self.lock2 = threading.Lock()
        self.lock2.acquire()

    def first(self, printFirst: "Callable[[], None]") -> None:
        # No lock needed — first() runs freely.
        printFirst()
        # Release lock1 → unblocks second() which is waiting to acquire it.
        self.lock1.release()

    def second(self, printSecond: "Callable[[], None]") -> None:
        # Block here: try to acquire lock1, which is currently held (locked).
        # This call returns only after first() releases lock1.
        self.lock1.acquire()
        printSecond()
        # Release lock2 → unblocks third() which is waiting to acquire it.
        self.lock2.release()

    def third(self, printThird: "Callable[[], None]") -> None:
        # Block here: try to acquire lock2, which is currently held (locked).
        # This call returns only after second() releases lock2.
        self.lock2.acquire()
        printThird()


class FooSemaphore:
    def __init__(self):
        # Semaphore holds an internal COUNTER (starts at 0).
        # acquire() decrements the counter; if it would go below 0, the
        # thread BLOCKS until another thread calls release() to increment it.
        # release() increments the counter, waking a blocked thread.
        self.sem1 = threading.Semaphore(0)  # counter = 0 → second() blocks on acquire()
        self.sem2 = threading.Semaphore(0)  # counter = 0 → third()  blocks on acquire()

    def first(self, printFirst: "Callable[[], None]") -> None:
        printFirst()
        # Increment sem1 counter (0 → 1) → wakes second() if it's blocked.
        self.sem1.release()

    def second(self, printSecond: "Callable[[], None]") -> None:
        # Decrement sem1 counter (1 → 0). If counter is 0, block until release().
        # Guarantees second() waits for first() to call sem1.release().
        self.sem1.acquire()
        printSecond()
        # Increment sem2 counter (0 → 1) → wakes third() if it's blocked.
        self.sem2.release()

    def third(self, printThird: "Callable[[], None]") -> None:
        # Decrement sem2 counter. Blocks until second() calls sem2.release().
        self.sem2.acquire()
        printThird()
