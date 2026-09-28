# HackerRank Practice Test — Questions & Answers

Session date: 2026-09-20

---

## 1. Data Structures — erase from beginning or end in O(1)

**Q:** Which data structure can erase from its beginning or its end in O(1) time?
vector / deque / stack / segment tree

**A: `deque`**

Double-ended queue. O(1) push/pop at both ends.

- `vector` — O(1) at back only; front erase is O(n) (shift everything)
- `stack` — one end only, no front access
- `segment tree` — range query structure, O(log n)

---

## 2. Good URI Design (pick one or more)

**Q:** Which of the following are true regarding good URI design?

**A: 1, 3, 5, 7**

| Statement | Verdict | Why |
|---|---|---|
| URIs should never be changed | ✅ | "Cool URIs don't change" (W3C) |
| URIs must be constructed by the client | ❌ | HATEOAS — server supplies links |
| URIs should be short in length | ✅ | Short, readable, guessable |
| URIs should be case-sensitive | ❌ | Use lowercase; avoid case dependence |
| HTTP verbs instead of operation names in URIs | ✅ | `GET /users/1`, not `/getUser?id=1` |
| Use spaces when designing a URI | ❌ | Never — use hyphens |
| Redirection must be used if a URI change is required | ✅ | 301 Moved Permanently |

---

## 3. SQL — Count the Employees

**Q:** Find companies with more than 10000 employees. Print IDs, ordered by ID.
Table `COMPANY(ID, NAME, EMPLOYEES)`.

```sql
SELECT ID FROM COMPANY WHERE EMPLOYEES > 10000 ORDER BY ID;
```

---

## 4. FizzBuzz

**Q:** For every integer `i` from 1 to `n`: print `FizzBuzz` if divisible by 3 and 5, `Fizz` if only 3, `Buzz` if only 5, else `i`.

```python
def fizzBuzz(n):
    for i in range(1, n + 1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
```

Check `% 15` first — it's the intersection of both conditions.

---

## 5. `rel="prefetch"` in `<link>`

**Q:** What is the need to use `rel="prefetch"`?

**A: It helps to load the resource that will be used in future navigation.**

- `rel="preload"` — current page resources, high priority
- `rel="prefetch"` — next-navigation resources, low priority, fetched when idle
- `rel="dns-prefetch"` — DNS lookup only

---

## 6. HTML5 `required` attribute (pick one or more)

```html
<form method="post" action="">
  <input type="text" required>
  <button type="submit">Submit</button>
</form>
```

**A: statements 2 and 3**

| Statement | Verdict | Why |
|---|---|---|
| Checks emptiness on the **server** side | ❌ | `required` is client-side HTML5 validation only; never reaches the server. Always re-validate server-side anyway |
| Checks on the **client** side when submitted | ✅ | Browser blocks submit, fires the `invalid` event |
| Submit button can be clicked even if empty | ✅ | Nothing disables it; the click registers, submission is blocked |
| An `<alert>message</alert>` is created; click OK then fill in | ❌ | Not a real tag, and it's a native validation bubble — not a JS `alert()` |

---

## 7. CSS3 Pseudo-elements — invalid declarations

**Q:** Select any invalid declaration for a pseudo-element.

**A: `span::last-line` and `.header::after-first-line`** — neither exists.

Valid pseudo-elements: `::first-line`, `::first-letter`, `::before`, `::after`, `::selection`, `::placeholder`, `::marker`, `::backdrop`.

Side note: `::first-line` on a `span` is also pointless — it only applies to block containers.

---

## 8. CSS3 Attribute Selector — valid statements

**A:**
```css
a[href^="#"] { background-color: gold; }   /* href starts with # */
a[href]      { background-color: gold; }   /* href exists */
```

Valid operators: `=` exact, `~=` word in list, `|=` exact-or-prefix-hyphen, `^=` starts with, `$=` ends with, `*=` contains.

`@=` and `&=` do not exist.

---

## 9. HTML5 Advantages — new items introduced

**A: all of them**

- Drag and drop — `draggable` attribute + drag events
- 2D drawing on a web page — `<canvas>`
- Timed media playback — `<audio>`, `<video>`
- New semantics — `<section>`, `<article>`, `<footer>`, `<nav>`, `<header>`

---

## 10. HTTP POST — which choice is INCORRECT

**A: "POST requests are cacheable by default."**

POST responses are cacheable only with explicit freshness headers (`Cache-Control`, `Expires`). GET and HEAD are cacheable by default.

Correct statements: POST adds a child resource under a collection; POST is not idempotent (n requests create n resources with n different URIs); POST is used for create operations.

---

## 11. Recurrence Time Complexity

**Q:** `T(n) = T(n-1) + 2n - 1` for `n > 0`, `T(n) = 0` for `n = 0`.

**A: O(n²)**

Unrolls into the sum of the first n odd numbers: `1 + 3 + 5 + ... + (2n-1)`, which is exactly `n²`.

Check: `T(0)=0`, `T(1)=1`, `T(2)=4`, `T(3)=9`.

---

## 12. Content Security Policy

**Q:** A banking site wants all content to originate from its own origin (including subdomains). Most appropriate CSP value?

**A: `default-src 'self'`**

`'self'` = same origin (scheme + host + port). `default-src` acts as the fallback for all resource types.

- `media-src site.com` — audio/video only
- `default-src 'none'` — blocks everything, site breaks
- `img-src *` — images from anywhere, opposite of the goal

---

## 13. Man In The Middle Attack

**Q:** What cryptographic method can be used as a parameter in a web request to ensure the message was not tampered with in transit?

**A: Hashing**

Hash is sent as a request parameter; the receiver recomputes and compares. Mismatch means tampered.

- Encoding — not cryptographic, reversible by anyone
- Encryption — confidentiality, not integrity on its own

In production use **HMAC** (keyed hash) — with a plain hash the attacker just recomputes it after tampering.

---

## 14. Transaction Vulnerability

**Q:** Account A and B both start at 500 USD. Multiple simultaneous 500 USD transfers from A to B with increasing thread counts. After the process, B has 1500 and A has 0. Which vulnerability?

**A: Race condition**

Classic TOCTOU (time-of-check to time-of-use). Concurrent threads all read `balance = 500`, all pass the check, all debit.

Fix: `SELECT ... FOR UPDATE` row lock, or a single atomic conditional update.

---

## 15. REST: HTTP Methods — same response regardless of invocation count

**A: GET, PUT, HEAD** (the idempotent methods)

- POST — not idempotent; n calls create n resources
- PATCH — not idempotent by spec. Can be (`{"status":"done"}`), but increments aren't.

---

## 16. ETag Header

**Q:** An API uses ETag headers for caching. Which statement is true?

**A:** "When the client makes a subsequent request, it includes the received ETag value in the **`If-None-Match`** header. The API compares it to the current hash value of the resource."

Wrong options: `If-Modified-Since` takes a **date**, not an ETag; a timestamp in the header is `Last-Modified`, not ETag.

How it works:
1. Server sends `ETag: "abc123"` — an opaque version identifier
2. Client resends it as `If-None-Match: "abc123"`
3. Unchanged → `304 Not Modified`, no body, bandwidth saved
4. Also enables optimistic concurrency via `If-Match` — prevents lost updates

Weak (`W/"abc"`) = semantically equal; strong = byte-identical.

---

## 17. Command Substitution

**Q:** Using command substitution, how would you display the value of the present working directory?

**A: `echo $(pwd)`**

`$(cmd)` *is* command substitution.

- `pwd | echo` — prints nothing; `echo` ignores stdin
- `echo pwd` — prints the literal string "pwd"
- `$pwd` — variable expansion, empty

---

## 18. UDP vs TCP

**Q:** Which transport protocol is used in VoIP communication and why?

**A: UDP, because it is connectionless oriented and uses less bandwidth.**

VoIP needs low latency. UDP has no handshake, no retransmit, and an 8-byte header vs TCP's 20. A dropped packet is a tiny audio glitch; a TCP retransmit is worse — delayed audio is useless.

---

## 19. Defect Triage

**Q:** What are the goals of defect triage meetings?

**A: Prioritize defects**

Triage = rank by severity/impact, then decide fix-now vs defer vs reject. The other options (defer, scrap, implement) are *outcomes* of triage, not its goal.

---

## 20. SQL — List the Course Names

**Q:** Return professor names and the courses they teach or have taught. Any order, no duplicate rows.

Schema: `PROFESSOR(ID, NAME, DEPARTMENT_ID, SALARY)`, `DEPARTMENT(ID, NAME)`, `COURSE(ID, NAME, DEPARTMENT_ID, CREDITS)`, `SCHEDULE(PROFESSOR_ID, COURSE_ID, SEMESTER, YEAR)`

```sql
SELECT DISTINCT p.NAME, c.NAME
FROM SCHEDULE s
JOIN PROFESSOR p ON p.ID = s.PROFESSOR_ID
JOIN COURSE c ON c.ID = s.COURSE_ID;
```

`DISTINCT` removes duplicates (same professor/course across different semesters). `SCHEDULE` is the bridge table — an inner join drops professors who never taught, which matches the expected output.

---

## 21. REST API: League Earnings

**Q:** `GET https://jsonmock.hackerrank.com/api/football_teams?league=<league_name>&page=<num>`

Ticket price by `total_silverware_count`: `>40` → 1.5, `>25` → 1.25, `>10` → 1, `<=10` → 0.5 USD.
Return total league earnings and average revenue per match. Each team plays every other team twice (home and away). Floor both values.

```python
import math
import requests

def leagueEarnings(league):
    url = "https://jsonmock.hackerrank.com/api/football_teams"
    clubs, page, maxPage = [], 1, 1
    while page <= maxPage:
        res = requests.get(url, params={"league": league, "page": page}).json()
        maxPage = res["total_pages"]
        clubs.extend(res["data"])
        page += 1

    perMatch = 0.0
    for club in clubs:
        silver = club["total_silverware_count"]
        if silver > 40:
            price = 1.5
        elif silver > 25:
            price = 1.25
        elif silver > 10:
            price = 1.0
        else:
            price = 0.5
        perMatch += club["stadium_capacity"] * price

    n = len(clubs)
    total = perMatch * (n - 1)
    totalMatch = n * (n - 1)
    average = total / totalMatch if totalMatch else 0
    return [math.floor(total), math.floor(average)]
```

**The catch:** each club earns `capacity × price` **per home match**, and hosts `n - 1` home matches. Forgetting the `(n - 1)` factor gives an answer ~19× too small.

Verified against the live API:
- EPL — n=20, total `13996649`, avg `36833`
- EFL League One — n=10, total `553279`, avg `6147`

`params=` handles URL-encoding of spaces and parens in `English Premier League (EPL)`.

---

## 22. Maximum Array Correlation

**Q:** Correlation = sum of all `b[i]` where `b[i] > a[i]`. Rearrange `b` (not `a`) to maximize it.
Constraints: `1 <= n <= 2×10^5`, `1 <= a[i], b[i] <= 10^9`.

Solution file: [`maxArrayCorrelation.py`](maxArrayCorrelation.py)

```python
def getMaxArrayCorrelation(a, b):
    a = sorted(a)
    b = sorted(b)

    # max number of b values that can each beat a distinct a
    i = 0
    k = 0
    for v in b:
        if v > a[i]:
            k += 1
            i += 1

    # if any k values of b can be matched, the k largest can too
    total = 0
    for j in range(len(b) - k, len(b)):
        total += b[j]

    return total
```

**Two insights:**

1. **Feasibility is sorted-vs-sorted.** To match k values of `b`, sort them ascending and pair against the k *smallest* `a` values sorted ascending. Need `S[j] > a[j]` for every j.
2. **If any k values work, the k largest work.** Swapping an element for a bigger one preserves every comparison and raises the sum. So only the *count* k matters — the values are always b's top k. No subset search needed.

Greedy count is correct because a `b` value that can't beat the smallest remaining `a` can't beat any remaining `a`, so discarding it costs nothing.

**Complexity:** O(n log n) time (sorts dominate), O(n) space (two `sorted()` copies; use `.sort()` in place for O(1) extra).

Verified: `a=[1,4,2,1,3], b=[2,3,1,2,2]` → **7**; `a=[1,9,4,2], b=[8,4,3,1]` → **15**; `a=[1,2,3,4,5], b=[3,5,4,6,2]` → **20**
