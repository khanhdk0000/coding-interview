from typing import List


def count_le(arr: List[int], target: int) -> int:
    # Number of elements <= target in sorted arr.
    # Find first index whose value > target; that index = the count.
    lo, hi = 0, len(arr)  # answer is somewhere in [lo, hi]
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] <= target:
            lo = mid + 1      # mid is counted, answer is to the right
        else:
            hi = mid          # mid is too big, but could be the first too-big one
    return lo


def triplets(a: List[int], b: List[int], c: List[int]) -> int:
    # "Distinct" triplets: remove duplicates, then sort so we can binary search.
    a = sorted(set(a))
    b = sorted(set(b))
    c = sorted(set(c))

    total = 0
    for q in b:
        count_a = count_le(a, q)  # how many p in a with p <= q
        count_c = count_le(c, q)  # how many r in c with r <= q
        total += count_a * count_c    # every p pairs with every r
    return total


if __name__ == '__main__':
    assert triplets([3, 5, 7], [3, 6], [4, 6, 9]) == 4
    assert triplets([1, 3, 5], [2, 3], [1, 2, 3]) == 8
    assert triplets([1, 4, 5], [2, 3, 3], [1, 2, 3]) == 5
    assert triplets([1, 3, 5, 7], [5, 7, 9], [7, 9, 11, 13]) == 12

    import random
    rng = random.Random(0)
    for _ in range(500):
        a = [rng.randint(1, 8) for _ in range(rng.randint(1, 6))]
        b = [rng.randint(1, 8) for _ in range(rng.randint(1, 6))]
        c = [rng.randint(1, 8) for _ in range(rng.randint(1, 6))]
        brute = len({(p, q, r) for p in a for q in b for r in c if p <= q >= r})
        assert triplets(a, b, c) == brute, (a, b, c)
    print("ok")
