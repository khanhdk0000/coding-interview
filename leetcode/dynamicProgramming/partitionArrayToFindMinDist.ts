function minimumDifference(nums: number[]): number {
  const n = nums.length;
  const sum = nums.reduce((acc, val) => acc + val, 0);
  const half = sum / 2;

  const dp = new Array(n + 1).fill(0).map(() => new Array(half + 1).fill(0));

  for (let i = 1; i <= n; i++) {
    for (let j = 1; j <= half; j++) {
      if (j >= nums[i - 1]) {
        dp[i][j] = Math.max(
          dp[i - 1][j],
          dp[i - 1][j - nums[i - 1]] + nums[i - 1]
        );
      } else {
        dp[i][j] = dp[i - 1][j];
      }
    }
  }

  return sum - 2 * dp[n][half];
}
