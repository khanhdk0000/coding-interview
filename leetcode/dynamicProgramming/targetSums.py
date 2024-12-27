from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
        
        # If target is out of feasible range or if (total_sum + target) is odd -> no solution
        if abs(target) > total_sum or (total_sum + target) % 2 != 0:
            return 0
        
        # We need to find the number of subsets that sum to subSum
        subSum = (total_sum + target) // 2
        
        # dp[x] will store number of ways to form sum x
        dp = [0] * (subSum + 1)
        dp[0] = 1  # One way to get sum 0 -> choose nothing
        
        for num in nums:
            # Update dp in reverse so we don't use the same num multiple times
            for j in range(subSum, num - 1, -1):
                dp[j] += dp[j - num]
        
        return dp[subSum]

sol = Solution()
print(sol.findTargetSumWays([1, 1, 1, 1, 1], 3))  # 5