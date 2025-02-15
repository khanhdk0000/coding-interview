from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        uniqueMap = {}
        uniqueCount = 0
        for i in range(len(nums)):
            if nums[i] not in uniqueMap:
                uniqueMap[nums[i]] = 1
                nums[uniqueCount] = nums[i]
                uniqueCount += 1
        return uniqueCount