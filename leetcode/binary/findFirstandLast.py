from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lower = self.find_lower_bound(nums, target)
        upper = self.find_upper_bound(nums, target)
        return [lower, upper]

    def find_lower_bound(self, nums, target):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                right = mid
        return left if nums and nums[left] == target else -1

    def find_upper_bound(self, nums, target):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2 + 1
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid
        return right if nums and nums[right] == target else -1
