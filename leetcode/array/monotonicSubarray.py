from typing import List
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        maxIncrease = 1
        maxDecrease = 1
        curIncrease = 1
        curDecrease = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                curIncrease += 1
                curDecrease = 1
            elif nums[i] < nums[i-1]:
                curDecrease += 1
                curIncrease = 1
            else:
                curIncrease = 1
                curDecrease = 1
            maxIncrease = max(maxIncrease, curIncrease)
            maxDecrease = max(maxDecrease, curDecrease)
        
        return max(maxIncrease, maxDecrease)