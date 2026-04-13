from typing import List

# LeetCode 188 — Best Time to Buy and Sell Stock IV
#
# At most k transactions (buy + sell = 1 transaction).
# Must sell before buying again.
#
# DP STATE:
#   buy[j]  = max cash after the j-th BUY  (stock currently held)
#   sell[j] = max cash after the j-th SELL (no stock held)
#
# TRANSITION per day per transaction slot j:
#   buy[j]  = max(buy[j],  sell[j-1] - price)  ← buy today (use prev sell's profit)
#   sell[j] = max(sell[j], buy[j]    + price)  ← sell today
#
# BASE CASE:
#   sell[-1] = 0  (no prior transaction → 0 starting cash)
#   buy/sell initialised to -inf (not yet reachable)
#
# OPTIMISATION:
#   If k >= n//2, unlimited transactions are effectively allowed.
#   Use greedy: sum all positive price differences.
#
# Time  : O(n * k)   — n days × k transaction slots
# Space : O(k)       — two arrays of length k


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        # ── Special case: unlimited transactions (greedy) ─────────────────────
        if k >= n // 2:
            return sum(max(prices[i + 1] - prices[i], 0) for i in range(n - 1))

        # ── General DP ────────────────────────────────────────────────────────
        INF = float("inf")
        buy = [-INF] * k  # buy[j]  = best cash after j-th buy
        sell = [-INF] * k  # sell[j] = best cash after j-th sell

        for price in prices:
            for j in range(k):
                # Cash available before this buy:
                #   j=0 → no prior sell, start with 0 cash
                #   j>0 → profit from the (j-1)-th sell
                prev_sell = 0 if j == 0 else sell[j - 1]

                buy[j] = max(buy[j], prev_sell - price)
                sell[j] = max(sell[j], buy[j] + price)

        # Best profit is the last sell (or 0 if no trade is profitable)
        return max(0, sell[k - 1])
