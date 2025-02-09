from typing import List
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        totalPairs = n * (n - 1) // 2
        countMap = {}
        for i, val in enumerate(nums):
            diff = i - val
            countMap[diff] = countMap.get(diff, 0) + 1
        goodPairs = 0
        for diff, count in countMap.items():
            goodPairs += count * (count - 1) // 2
        return totalPairs - goodPairs