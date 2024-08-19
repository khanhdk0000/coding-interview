function minSteps(n: number): number {
  let dp = new Array(n + 1).fill(0);
  // find smallest prime factor of n
  for (let i = 2; i <= n; i++) {
    dp[i] = i;
    for (let j = 2; j <= Math.sqrt(i); j++) {
      if (i % j === 0) {
        dp[i] = dp[j] + dp[i / j];
        break;
      }
    }
  }

  return dp[n];
}
