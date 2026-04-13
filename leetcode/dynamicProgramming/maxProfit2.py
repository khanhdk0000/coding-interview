from typing import List

# LeetCode 122 — Best Time to Buy and Sell Stock II
# Unlimited transactions — sell before buying again.
#
# Difference from LC 121:
#   LC 121 (1 tx):    hold = max(hold,    0 - price)   ← cash before buy is always 0
#   LC 122 (unlimited): hold = max(hold, free - price)  ← can rebuy using prior sell profit
#
# STATES:
#   hold = max cash while HOLDING stock
#   free = max cash while NOT holding stock (can buy again)
#
# TRANSITIONS:
#   hold = max(hold, free - price)   ← keep holding  OR  buy today using free cash
#   free = max(free, hold + price)   ← stay free     OR  sell today
#
# Time  : O(n)  — single pass
# Space : O(1)  — two scalar variables (not arrays!)


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = float("-inf")  # haven't bought yet
        free = 0  # haven't traded, 0 cash

        for price in prices:
            hold = max(hold, free - price)  # ← key diff from LC121: use free, not 0
            free = max(free, hold + price)

        return free
