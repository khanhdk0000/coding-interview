from typing import List
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum = 0
        min_sum = 0
        max_sum_so_far = 0
        min_sum_so_far = 0
        for num in nums:
            max_sum = max(max_sum + num, num)
            min_sum = min(min_sum + num, num)
            max_sum_so_far = max(max_sum, max_sum_so_far)
            min_sum_so_far = min(min_sum, min_sum_so_far)
        return max(max_sum_so_far, abs(min_sum_so_far))

sol = Solution()
print(sol.maxAbsoluteSum([1, -3, 2, 3, -4])) # 5
# print(sol.maxAbsoluteSum([2, -5, 1, -4, 3, -2])) # 8