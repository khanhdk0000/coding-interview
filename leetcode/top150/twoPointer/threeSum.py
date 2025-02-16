from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        # Use two sum to solve three sum
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            twoSumRes = self.twoSum(nums[i+1:], -nums[i])
            for twoSum in twoSumRes:
                res.append([nums[i]] + twoSum)
        # Remove duplicates
        res = list(set([tuple(sorted(x)) for x in res]))
        return res

        return [-1, -1, -1]
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        res = []
        for i in range(len(nums)):
            if target - nums[i] in numMap:
                res.append([nums[numMap[target - nums[i]]], nums[i]])
            numMap[nums[i]] = i
        return res