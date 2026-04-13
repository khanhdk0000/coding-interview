from typing import List

# LeetCode 121 — Best Time to Buy and Sell Stock
# At most 1 transaction (buy once, sell once).
#
# DP TYPE: Linear DP (1D), two states
#
# STATES:
#   hold = max cash while HOLDING the stock
#   free = max cash while NOT holding the stock
#
# TRANSITIONS (per day):
#   hold = max(hold,        0 - price )   ← keep holding  OR  buy today (cash was 0)
#   free = max(free,  hold + price    )   ← stay free     OR  sell today
#
# Why `0 - price` and not `free - price`?
#   Only 1 transaction allowed → you can never sell then rebuy.
#   So cash before the only buy is always 0.
#
# BASE CASES:
#   hold = -inf  (haven't bought yet, state unreachable)
#   free =  0    (haven't traded, 0 profit)
#
# Time  : O(n)  — single pass through prices
# Space : O(1)  — only two variables


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = float("-inf")  # max cash while holding stock
        free = 0  # max cash while not holding stock

        for price in prices:
            hold = max(hold, -price)  # buy today costs `price` from 0 cash
            free = max(free, hold + price)  # sell today earns `price`

        return free
