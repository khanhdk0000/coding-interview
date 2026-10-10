from collections import Counter
from typing import List


def countTriplets(arr: List[int], r: int) -> int:
    # Treat each x as the middle: pairs = (# of x/r before) * (# of x*r after).
    left = Counter()
    right = Counter(arr)
    count = 0
    for x in arr:
        right[x] -= 1
        if x % r == 0:
            count += left[x // r] * right[x * r]
        left[x] += 1
    return count


if __name__ == '__main__':
    assert countTriplets([1, 4, 16, 64], 4) == 2
    assert countTriplets([1, 2, 2, 4], 2) == 2
    assert countTriplets([1, 3, 9, 9, 27, 81], 3) == 6
    assert countTriplets([1, 1, 1, 1], 1) == 4  # C(4,3), r=1 edge
    assert countTriplets([1, 5, 5, 25, 125], 5) == 4
    print("ok")
