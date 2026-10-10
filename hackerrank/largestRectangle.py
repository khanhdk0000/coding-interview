from typing import List


def largestRectangle(h: List[int]) -> int:
    # Monotonic stack of indices with increasing heights.
    # When a shorter bar arrives, each popped bar has found its right limit
    # (current i) and its left limit (new stack top), so its widest rectangle is known.
    stack = []
    best = 0
    for i, height in enumerate(h + [0]):  # trailing 0 flushes the stack at the end
        while stack and h[stack[-1]] >= height:
            top = h[stack.pop()]
            left = stack[-1] if stack else -1
            best = max(best, top * (i - left - 1))
        stack.append(i)
    return best


if __name__ == '__main__':
    assert largestRectangle([1, 2, 3, 4, 5]) == 9
    assert largestRectangle([3, 2, 3]) == 6
    assert largestRectangle([2, 1, 5, 6, 2, 3]) == 10
    assert largestRectangle([5]) == 5
    assert largestRectangle([2, 2, 2]) == 6
    assert largestRectangle([5, 4, 3, 2, 1]) == 9

    import random
    rng = random.Random(0)
    for _ in range(500):
        a = [rng.randint(1, 6) for _ in range(rng.randint(1, 10))]
        brute = max(min(a[i:j + 1]) * (j - i + 1) for i in range(len(a)) for j in range(i, len(a)))
        assert largestRectangle(a) == brute, a
    print("ok")
