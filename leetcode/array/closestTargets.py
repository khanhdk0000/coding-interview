from typing import List


class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        """
        LeetCode 2515 - Shortest Distance to Target String in a Circular Array

        Approach:
            Single pass over all indices. For each index i where words[i] == target,
            compute both the clockwise distance (i - startIndex) % n and the
            counter-clockwise distance (startIndex - i) % n, then track the minimum.

        Time Complexity:  O(n) — one linear scan through the array.
        Space Complexity: O(1) — only a constant number of variables used.
        """
        n = len(words)
        min_dist = float("inf")

        for i in range(n):
            if words[i] == target:
                clockwise = (i - startIndex) % n
                counter_clockwise = (startIndex - i) % n
                min_dist = min(min_dist, clockwise, counter_clockwise)

        return min_dist if min_dist != float("inf") else -1
