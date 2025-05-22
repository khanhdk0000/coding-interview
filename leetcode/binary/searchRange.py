from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLeft(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        left_index = findLeft(nums, target)
        right_index = left_index
        while right_index < len(nums) and nums[right_index] == target:
            right_index += 1
        right_index -= 1
        if left_index < len(nums) and nums[left_index] == target:
            return [left_index, right_index]
        else:
            return [-1, -1]