import heapq
from typing import List


def activityNotifications(expenditure: List[int], d: int) -> int:
    # Two heaps hold the window split in half:
    #   lo = max-heap of the smaller half, stored as (-value, -index)
    #   hi = min-heap of the larger half, stored as (value, index)
    # Keeping the index makes every entry unique, so we always know which heap
    # an outgoing day sits in. Removal is lazy: dead entries (index < start)
    # get popped only when they reach the top.
    lo, hi = [], []
    lo_n = hi_n = 0  # live sizes (heaps may also hold dead entries)
    start = 0        # window = indices [start, start + d)

    def prune():
        while lo and -lo[0][1] < start:
            heapq.heappop(lo)
        while hi and hi[0][1] < start:
            heapq.heappop(hi)

    def rebalance():
        # keep lo_n == hi_n or lo_n == hi_n + 1
        nonlocal lo_n, hi_n
        if lo_n > hi_n + 1:
            v, j = heapq.heappop(lo)
            heapq.heappush(hi, (-v, -j))
            lo_n, hi_n = lo_n - 1, hi_n + 1
        elif lo_n < hi_n:
            v, j = heapq.heappop(hi)
            heapq.heappush(lo, (-v, -j))
            lo_n, hi_n = lo_n + 1, hi_n - 1
        prune()

    def lo_top():
        return (-lo[0][0], -lo[0][1])

    def add(j):
        nonlocal lo_n, hi_n
        x = (expenditure[j], j)
        if not lo or x <= lo_top():
            heapq.heappush(lo, (-x[0], -x[1]))
            lo_n += 1
        else:
            heapq.heappush(hi, x)
            hi_n += 1
        rebalance()

    def remove(j):
        nonlocal lo_n, hi_n, start
        x = (expenditure[j], j)
        if x <= lo_top():
            lo_n -= 1
        else:
            hi_n -= 1
        start = j + 1  # marks x dead
        prune()
        rebalance()

    for j in range(d):
        add(j)

    notices = 0
    for i in range(d, len(expenditure)):
        # 2 * median, kept as an int
        if d % 2:
            double_median = 2 * lo_top()[0]
        else:
            double_median = lo_top()[0] + hi[0][0]
        if expenditure[i] >= double_median:
            notices += 1
        remove(i - d)
        add(i)
    return notices


if __name__ == '__main__':
    assert activityNotifications([10, 20, 30, 40, 50], 3) == 1
    assert activityNotifications([2, 3, 4, 2, 3, 6, 8, 4, 5], 5) == 2
    assert activityNotifications([1, 2, 3, 4, 4], 4) == 0
    assert activityNotifications([1, 3, 5, 7], 2) == 1

    # compare against brute force on random input, lots of duplicates, all d
    import random
    from statistics import median

    def brute(e, d):
        return sum(e[i] >= 2 * median(e[i - d:i]) for i in range(d, len(e)))

    rng = random.Random(0)
    for _ in range(2000):
        n = rng.randint(1, 15)
        e = [rng.randint(0, 6) for _ in range(n)]
        d = rng.randint(1, n)
        assert activityNotifications(e, d) == brute(e, d), (e, d)
    print("ok")
