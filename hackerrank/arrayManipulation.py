from typing import List


def arrayManipulation(n: int, queries: List[List[int]]) -> int:
    # Difference array: +k at a, -k after b. Prefix sum rebuilds real values.
    diff = [0] * (n + 2)
    for a, b, k in queries:
        diff[a] += k
        diff[b + 1] -= k

    best = cur = 0
    for v in diff:
        cur += v
        best = max(best, cur)
    return best


if __name__ == '__main__':
    assert arrayManipulation(10, [[1, 5, 3], [4, 8, 7], [6, 9, 1]]) == 10
    assert arrayManipulation(5, [[1, 2, 100], [2, 5, 100], [3, 4, 100]]) == 200
    print("ok")
