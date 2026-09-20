from typing import List


def findNextGreaterElementsWithDistance(readings: List[int]) -> List[List[int]]:
    """Next strictly greater element to the right, plus index distance."""
    res = [[-1, -1] for _ in readings]  # fresh lists: [[-1,-1]] * n shares one object
    stack = []  # indices, values non-increasing
    for i, x in enumerate(readings):
        while stack and readings[stack[-1]] < x:
            j = stack.pop()
            res[j] = [x, i - j]
        stack.append(i)
    return res


if __name__ == "__main__":
    assert findNextGreaterElementsWithDistance([2, 1, 2, 4, 3]) == [[4, 3], [2, 1], [4, 1], [-1, -1], [-1, -1]]
    assert findNextGreaterElementsWithDistance([5]) == [[-1, -1]]
    assert findNextGreaterElementsWithDistance([]) == []
    assert findNextGreaterElementsWithDistance([3, 3, 3]) == [[-1, -1], [-1, -1], [-1, -1]]  # equal is not greater
    assert findNextGreaterElementsWithDistance([1, 2, 3]) == [[2, 1], [3, 1], [-1, -1]]
    assert findNextGreaterElementsWithDistance([3, 2, 1]) == [[-1, -1], [-1, -1], [-1, -1]]
    assert findNextGreaterElementsWithDistance([-5, -9, -1]) == [[-1, 2], [-1, 1], [-1, -1]]  # -1 is a real value here
    print("ok")
