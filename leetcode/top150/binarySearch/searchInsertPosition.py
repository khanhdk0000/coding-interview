from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # search for the target in the sorted array
        # if the target is not found, return the index where it should be inserted
        # binary search
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left