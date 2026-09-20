from typing import List


def mergeHighDefinitionIntervals(intervals: List[List[int]]) -> List[List[int]]:
    """Merge overlapping intervals, return sorted by start."""
    if len(intervals) <= 1:
        return intervals
    intervals.sort()
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if start > merged[-1][1]:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)
    return merged


if __name__ == "__main__":
    assert mergeHighDefinitionIntervals([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert mergeHighDefinitionIntervals([]) == []
    assert mergeHighDefinitionIntervals([[5, 10]]) == [[5, 10]]
    assert mergeHighDefinitionIntervals([[8, 10], [1, 3], [2, 6]]) == [[1, 6], [8, 10]]  # unsorted input
    assert mergeHighDefinitionIntervals([[1, 10], [2, 3]]) == [[1, 10]]  # fully contained
    assert mergeHighDefinitionIntervals([[1, 4], [4, 5]]) == [[1, 5]]  # touching
    assert mergeHighDefinitionIntervals([[1, 2], [1, 2]]) == [[1, 2]]  # duplicate
    print("ok")
