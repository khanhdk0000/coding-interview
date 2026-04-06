from typing import List

# LeetCode 11 — Container With Most Water
#
# Two-pointer approach:
#   - Start with the widest possible container (i=0, j=n-1).
#   - Area = width * min(height[i], height[j])
#   - The width shrinks as we move pointers inward, so to have any
#     chance of a larger area we MUST increase the height.
#   - Always move the pointer at the SHORTER line inward:
#       → keeping the taller side and moving inward is the only way
#         a future container could possibly be larger.
#   - Optimisation: skip lines that are even shorter than the current
#     bottleneck — they can never beat the current best height.
#
# Time  : O(n)  — each pointer moves at most n times total
# Space : O(1)  — only a fixed number of variables used


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        maxArea = 0

        while i < j:
            h = min(height[i], height[j])
            maxArea = max(maxArea, (j - i) * h)
            if height[i] < height[j]:
                while i < j and height[i] <= h:
                    i += 1
            else:
                while i < j and height[j] <= h:
                    j -= 1

        return maxArea
