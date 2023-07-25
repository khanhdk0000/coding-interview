from typing import List

"""
time O(n)
space O(1)
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, n, profit = 0, len(prices) - 1, 0
        while i < n:
            while (i < n and prices[i+1] <=  prices[i]):
                i += 1
            buy = prices[i]

            while(i < n and prices[i+1] >= prices[i]):
                i += 1
            sell = prices[i]
            profit += sell - buy
        return profit

input = [7,1,5,3,6,4]
sol = Solution()

print(sol.maxProfit(input))