from typing import List
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        dp = [0] * len(values)
        dp[0] = values[0]
        res = 0
        for i in range(1, len(values)):
            dp[i] = max(dp[i-1], values[i] + i)
            res = max(res, dp[i-1] + values[i] - i)
        return res
    
sol = Solution()
print(sol.maxScoreSightseeingPair([8,1,5,2,6])) # 11
print(sol.maxScoreSightseeingPair([1,2]))