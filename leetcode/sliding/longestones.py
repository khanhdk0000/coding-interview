from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        maxLength = 0
        while right < len(nums):
            if nums[right] == 0:
                k -= 1
            while k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
            maxLength = max(maxLength, right - left + 1)
            right += 1
        return maxLength


sol = Solution()
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(sol.longestOnes(nums, k))