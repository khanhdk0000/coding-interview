function strangePrinter(s: string): number {
  const n = s.length;
  const dp: number[][] = new Array(n).fill(0).map(() => new Array(n).fill(0));
  for (let i = n - 1; i >= 0; i--) {
    // Base case, 
    dp[i][i] = 1;
    for (let j = i + 1; j < n; j++) {
        if (s[i] === s[j]) {
        dp[i][j] = dp[i][j - 1];
      } else {
        // Find the minimum number of operations to print s[i:j]
        let min = Number.MAX_SAFE_INTEGER;
        for (let k = i; k < j; k++) {
          min = Math.min(min, dp[i][k] + dp[k + 1][j]);
        }
        dp[i][j] = min;
      }
    }
  }
  return dp[0][n - 1];
}
