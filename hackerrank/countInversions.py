from typing import List


def countInversions(arr: List[int]) -> int:
    # Merge sort. While merging, when right[j] goes before left[i],
    # it jumps over every remaining left element: that many inversions.
    def sort(a):
        if len(a) <= 1:
            return a, 0
        mid = len(a) // 2
        left, inv_l = sort(a[:mid])
        right, inv_r = sort(a[mid:])
        merged = []
        inv = inv_l + inv_r
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:  # <= : equal values are not inversions
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                inv += len(left) - i
                j += 1
        merged += left[i:]
        merged += right[j:]
        return merged, inv

    return sort(arr)[1]


if __name__ == '__main__':
    assert countInversions([1, 1, 1, 2, 2]) == 0
    assert countInversions([2, 1, 3, 1, 2]) == 4
    assert countInversions([5, 4, 3, 2, 1]) == 10
    assert countInversions([7]) == 0

    import random
    rng = random.Random(0)
    for _ in range(500):
        a = [rng.randint(1, 5) for _ in range(rng.randint(1, 12))]
        brute = sum(a[i] > a[j] for i in range(len(a)) for j in range(i + 1, len(a)))
        assert countInversions(a) == brute, a
    print("ok")
