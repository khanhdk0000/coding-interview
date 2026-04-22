from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for right in range(1, len(nums)):
            if nums[right] == 0 and nums[left] != 0:
                left = right
            if nums[right] != 0 and nums[left] == 0:
                nums[left] = nums[right]
                nums[right] = 0
                left += 1