"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
"""

from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[List[int]]:
        numMap = {}
        res = []
        for idx, val in enumerate(numbers):
            if target - val in numMap:
                res.append([val, target-val])
            if val not in numMap:
                numMap[val] = idx
        return res


    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        resSet = set()
        nums.sort()
        n = len(nums)
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]: # skip previous duplicate
                continue
            if nums[i] + nums[i + 1] + nums[i + 2] > 0:
                break
            if nums[i] + nums[n - 2] + nums[n - 1] < 0:
                continue
            listTwoSum = self.twoSum(nums[i+1:], 0 - nums[i])
            for s in listTwoSum:
                triplet = [nums[i]] + s
                sorted_triplet = tuple(sorted(triplet))
                if sorted_triplet not in resSet:
                    resSet.add(sorted_triplet)
                    res.append(triplet)
        return res

nums = [-1,0,1,2,-1,-4]
nums = [0,1,1]
sol = Solution()

print(sol.threeSum(nums))
