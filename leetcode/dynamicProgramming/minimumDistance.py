# LeetCode 1320 — Minimum Distance to Type a Word Using Two Fingers
#
# Keyboard layout (6 letters per row):
#   A B C D E F       row 0
#   G H I J K L       row 1
#   M N O P Q R       row 2
#   S T U V W X       row 3
#   Y Z               row 4
#
# letter c → row = (c-'A')//6, col = (c-'A')%6
# dist(a, b) = |row_a - row_b| + |col_a - col_b|  (Manhattan)
#
# DP state: dp[other] = min cost to have typed word[0..i],
#           with one finger on word[i] and the other on letter `other`.
#           Use index 26 to represent "finger not yet placed" (free).
#
# Transition when typing word[i+1] = nxt, current finger is on cur = word[i]:
#   Option 1 — move the `cur` finger to `nxt`:
#       new_dp[other] = min(new_dp[other], dp[other] + dist(cur, nxt))
#   Option 2 — move the `other` finger to `nxt`:
#       new_dp[cur]   = min(new_dp[cur],   dp[other] + dist(other, nxt))
#                                                       (0 if other==26, free start)
#
# Time  : O(n * 27)  = O(n)   — n = len(word), 27 possible `other` positions
# Space : O(27)               — only current dp row needed


class Solution:
    def minimumDistance(self, word: str) -> int:

        def pos(c: str):
            """Return (row, col) of letter c on the keyboard."""
            idx = ord(c) - ord("A")
            return idx // 6, idx % 6

        def dist(a: str, b: str) -> int:
            """Manhattan distance between letters a and b.
            If a is the sentinel '?' (not yet placed), cost is 0 (free start).
            """
            if a == "?":
                return 0
            r1, c1 = pos(a)
            r2, c2 = pos(b)
            return abs(r1 - r2) + abs(c1 - c2)

        # dp[other] = min cost so far, one finger on word[i], other on `other`
        # Use index 0..25 for letters A-Z, index 26 for "not placed yet"
        INF = float("inf")
        FREE = 26
        dp = [INF] * 27
        dp[FREE] = 0  # start: both fingers free, cost = 0

        for i in range(len(word) - 1):
            cur = word[i]
            nxt = word[i + 1]
            new_dp = [INF] * 27

            for other_idx in range(27):
                if dp[other_idx] == INF:
                    continue

                other = "?" if other_idx == FREE else chr(ord("A") + other_idx)
                cost = dp[other_idx]

                # Option 1: move finger on `cur` → `nxt` (other stays)
                new_dp[other_idx] = min(new_dp[other_idx], cost + dist(cur, nxt))

                # Option 2: move `other` finger → `nxt` (cur finger now becomes `other`)
                cur_idx = ord(cur) - ord("A")
                new_dp[cur_idx] = min(new_dp[cur_idx], cost + dist(other, nxt))

            dp = new_dp

        return min(dp)
