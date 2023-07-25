from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """       
        if k == 0:
            return
        while k > len(nums):
            k = k - len(nums)
        # trim = nums[len(nums)-k:]
        # nums[:] = nums[:-k]
        # nums[:] = trim + nums
        nums[:] = nums[-k:] + nums[:-k]


input = [1,2,3,4,5,6]
sol = Solution()
sol.rotate(input, 11)
print(input)
# [2,3,4,5,6,1]