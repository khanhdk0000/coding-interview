from typing import List

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        minDistance = len(nums)
        for i in range(len(nums)):
            if nums[i] == target:
                minDistance = min(minDistance, abs(i-start))
        return minDistance