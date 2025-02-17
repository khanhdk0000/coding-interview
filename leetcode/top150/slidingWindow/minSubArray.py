from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        sum = 0
        minLen = float('inf')
        while right < len(nums):
            sum += nums[right]
            right += 1
            while sum >= target:
                minLen = min(minLen, right - left)
                sum -= nums[left]
                left += 1
        return minLen if minLen != float('inf') else 0