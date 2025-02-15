from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        maxReach = 0
        steps = 0
        end = 0
        for i in range(n - 1):
            maxReach = max(maxReach, i + nums[i])
            if i == end:
                steps += 1
                end = maxReach
        return steps