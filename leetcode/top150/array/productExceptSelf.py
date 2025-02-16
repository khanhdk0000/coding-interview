from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1]*n
        left = 1
        right = 1
        for i in range(n):
            res[i] *= left
            left *= nums[i]
            res[n-i-1] *= right
            right *= nums[n-i-1]
        return res