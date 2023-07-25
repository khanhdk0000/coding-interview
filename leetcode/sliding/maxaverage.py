from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if k == 1:
            return max(nums)
        res = sum(nums[:k])
        prevSum = res
        for i in range(k, len(nums)):
            nextSum = prevSum - nums[i - k] + nums[i]
            # print(res, nextSum, k)
            res = max(res, nextSum)
            prevSum = nextSum
        return res / k


sol = Solution()
nums = [4,2,1,3,3]
k = 2
print(sol.findMaxAverage(nums, k))
