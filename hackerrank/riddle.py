from typing import List


def riddle(arr: List[int]) -> List[int]:
    # Same stack as largestRectangle: when arr[i] is popped we know the widest
    # window where it is the minimum. best[w] = largest such min for width w.
    n = len(arr)
    best = [0] * (n + 2)
    stack = []
    for i, x in enumerate(arr + [-1]):  # -1 sentinel flushes the stack (values >= 0)
        while stack and arr[stack[-1]] >= x:
            v = arr[stack.pop()]
            left = stack[-1] if stack else -1
            w = i - left - 1
            if v > best[w]:
                best[w] = v
        stack.append(i)
    # A min that covers width w also works for every smaller width.
    for w in range(n - 1, 0, -1):
        if best[w + 1] > best[w]:
            best[w] = best[w + 1]
    return best[1:n + 1]


if __name__ == '__main__':
    assert riddle([6, 3, 5, 1, 12]) == [12, 3, 3, 1, 1]
    assert riddle([2, 6, 1, 12]) == [12, 2, 1, 1]
    assert riddle([1, 2, 3, 5, 1, 13, 3]) == [13, 3, 2, 1, 1, 1, 1]
    assert riddle([3, 5, 4, 7, 6, 2]) == [7, 6, 4, 4, 3, 2]
    assert riddle([0]) == [0]

    import random
    rng = random.Random(0)
    for _ in range(500):
        a = [rng.randint(0, 6) for _ in range(rng.randint(1, 10))]
        brute = [max(min(a[i:i + w]) for i in range(len(a) - w + 1)) for w in range(1, len(a) + 1)]
        assert riddle(a) == brute, a
    print("ok")
