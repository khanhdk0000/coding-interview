function stoneGameII(piles: number[]): number {
  const n = piles.length;
  const dp = Array.from({ length: n + 1 }, () =>
    Array.from({ length: n + 1 }, () => 0)
  );
  const sum = Array.from({ length: n + 1 }, () => 0);
  for (let i = n - 1; i >= 0; i--) {
    sum[i] = sum[i + 1] + piles[i];
  }
  for (let i = n - 1; i >= 0; i--) {
    for (let m = 1; m <= n; m++) {
      if (i + 2 * m >= n) {
        dp[i][m] = sum[i];
      } else {
        for (let x = 1; x <= 2 * m; x++) {
          dp[i][m] = Math.max(dp[i][m], sum[i] - dp[i + x][Math.max(m, x)]);
        }
      }
    }
  }
  return dp[0][1];
}
