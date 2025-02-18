from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numMap = {}
        res = 0
        for num in nums:
            if num not in numMap:
                left = numMap.get(num -1, 0)
                right = numMap.get(num + 1, 0)
                cur = left + right + 1
                res = max(res, cur)
                numMap[num] = cur
                numMap[num - left] = cur
                numMap[num + right] = cur
        return res