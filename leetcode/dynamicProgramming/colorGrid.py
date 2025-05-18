MOD = 10**9 + 7
class Solution:
    def colorTheGrid(m: int, n: int) -> int:
        # 1. generate every valid column colouring
        patterns = []
        def dfs(col, row):
            if row == m:
                patterns.append(tuple(col))
                return
            for colour in (0, 1, 2):                 # 0-red, 1-green, 2-blue
                if row == 0 or colour != col[-1]:    # vertical check
                    col.append(colour)
                    dfs(col, row + 1)
                    col.pop()
        dfs([], 0)

        k = len(patterns)                            # ≤ 48 when m ≤ 5

        # 2. build adjacency - which columns differ row-wise
        compat = [[] for _ in range(k)]
        for i in range(k):
            for j in range(k):
                if all(patterns[i][r] != patterns[j][r] for r in range(m)):
                    compat[i].append(j)

        # 3. DP across columns
        dp = [1] * k                                 # first column
        for _ in range(n - 1):
            nxt = [0] * k
            for j in range(k):
                s = 0
                for t in compat[j]:
                    s += dp[t]
                nxt[j] = s % MOD
            dp = nxt

        return sum(dp) % MOD
