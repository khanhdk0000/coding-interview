from bisect import bisect_left
from typing import List


def _prev_smaller_pair(h):
    """For each i: nearest index left with h < h[i], and the next one before that.

    The second one is found by bisecting the strict suffix minima of the gap
    (p1[p], p), which are exactly the stack entries popped when p was pushed.
    Values along that list increase with index, so bisect finds the rightmost
    entry below h[i] in log time (C-level, so it stays cheap at n = 1e6).
    """
    n = len(h)
    p1 = [-1] * n
    p2 = [-1] * n
    stack = []  # (index, popped indices, their heights); dropped when popped
    for i, x in enumerate(h):
        popped = []
        while stack and h[stack[-1][0]] >= x:
            popped.append(stack.pop()[0])
        popped.reverse()  # index ascending, height ascending
        if stack:
            p, p_idx, p_val = stack[-1]
            p1[i] = p
            k = bisect_left(p_val, x)
            p2[i] = p_idx[k - 1] if k else p1[p]
        stack.append((i, popped, [h[j] for j in popped]))
    return p1, p2


def computeMaxRectangleAreaWithOneRemoval(heights: List[int]) -> int:
    """Largest histogram rectangle, optionally deleting one bar first."""
    n = len(heights)
    if n == 0:
        return 0
    p1, p2 = _prev_smaller_pair(heights)
    q1, q2 = _prev_smaller_pair(heights[::-1])
    # mirror the reversed-array answers back into original indices
    n1 = [n - 1 - q1[n - 1 - i] if q1[n - 1 - i] >= 0 else n for i in range(n)]
    n2 = [n - 1 - q2[n - 1 - i] if q2[n - 1 - i] >= 0 else n for i in range(n)]

    best = 0
    for i, height in enumerate(heights):
        left, right = p1[i], n1[i]
        best = max(best, height * (right - left - 1))  # no removal
        if left >= 0:  # delete the blocker on the left, widen to p2
            best = max(best, height * (right - p2[i] - 2))
        if right < n:  # delete the blocker on the right, widen to n2
            best = max(best, height * (n2[i] - left - 2))
    return best


if __name__ == "__main__":
    f = computeMaxRectangleAreaWithOneRemoval
    assert f([5, 5, 1, 5, 5]) == 20
    assert f([5]) == 5
    assert f([2, 2]) == 4
    assert f([]) == 0
    assert f([4, 5, 1, 5, 4]) == 16  # best height is below both neighbours of the gap
    assert f([0, 0]) == 0
    assert f([1, 2, 3, 4]) == 6  # nothing worth deleting
    print("ok")
