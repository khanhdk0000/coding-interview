from typing import List


class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        """
        LeetCode 2078 - Two Furthest Houses With Different Colors

        Key insight: the maximum-distance pair must include either the first
        house (i=0) or the last house (j=n-1). If the furthest valid pair
        didn't touch either end, we could extend it to one end for a larger
        distance — contradiction. So we only need two linear scans:
          1. Fix i=0,   scan j from the right for the first different color.
          2. Fix j=n-1, scan i from the left  for the first different color.

        Time Complexity : O(n)
        Space Complexity: O(1)
        """
        n = len(colors)
        res = 0

        # Fix left end at 0, find the rightmost house with a different color
        for j in range(n - 1, 0, -1):
            if colors[j] != colors[0]:
                res = j  # distance = j - 0 = j
                break

        # Fix right end at n-1, find the leftmost house with a different color
        for i in range(n - 1):
            if colors[i] != colors[n - 1]:
                res = max(res, n - 1 - i)
                break

        return res
