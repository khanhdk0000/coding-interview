"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""

from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numMap = {}
        for idx, val in enumerate(nums):
            if val not in numMap:
                numMap[val] = idx
            else:
                if abs(idx - numMap[val]) <= k:
                    return True
                else:
                    numMap[val] = idx
        return False


nums = [1,2,3,1]
k = 3
nums = [1,0,1,1]
k = 1
nums = [1,2,3,1,2,3]
k = 2

sol = Solution()


print(sol.containsNearbyDuplicate(nums, k))

