"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
"""

from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right, res = 0, 0, len(nums) + 1
        currentSum = nums[0]
        while left < len(nums) and right < len(nums):
            # print(currentSum, left, right)
            if currentSum >= target:
                res = min(res, right - left + 1)
                currentSum -= nums[left]
                left += 1
            elif currentSum < target:
                right += 1
                if right < len(nums):
                    currentSum += nums[right]
        return res if res != len(nums) + 1 else 0


target = 7
nums = [2,3,1,2,4,3]
target = 4
nums = [1,4,4]
target = 11
nums = [1,1,1,1,1,1,1,1]
# nums = [1,2,3,4,5]
sol = Solution()

print(sol.minSubArrayLen(target, nums))
