from typing import List


def maxSubsetSum(arr: List[int]) -> int:
    # House Robber. At each element: skip it (keep prev1) or take it (prev2 + x).
    # Starting at 0 = empty subset allowed, so all-negative arrays return 0.
    prev2 = prev1 = 0  # best sum up to i-2, best sum up to i-1
    for x in arr:
        skip = prev1         # don't take x: best so far stays
        take = prev2 + x     # take x: can't use previous, so add to best from 2 back
        best = max(skip, take)

        prev2 = prev1        # shift window forward by one
        prev1 = best
    return prev1


if __name__ == '__main__':
    assert maxSubsetSum([-2, 1, 3, -4, 5]) == 8
    assert maxSubsetSum([-2, -3, -1]) == 0
    assert maxSubsetSum([3, 7, 4, 6, 5]) == 13
    assert maxSubsetSum([2, 1, 5, 8, 4]) == 11
    assert maxSubsetSum([3, 5, -7, 8, 10]) == 15

    from itertools import combinations
    import random
    rng = random.Random(0)
    for _ in range(500):
        a = [rng.randint(-5, 5) for _ in range(rng.randint(1, 8))]
        brute = max(
            sum(a[i] for i in c)
            for k in range(len(a) + 1)
            for c in combinations(range(len(a)), k)
            if all(c[j + 1] - c[j] > 1 for j in range(len(c) - 1))
        )
        assert maxSubsetSum(a) == brute, a
    print("ok")
