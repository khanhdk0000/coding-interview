// Return the number of ways n can be expressed as the sum of the xth power of unique, natural numbers.
function numberOfWays(n: number, x: number): number {
    // Create a DP array with (n+1) elements initialized to 0
    let dp = new Array(n + 1).fill(0);
    dp[0] = 1; // There is one way to get the sum of 0: use no numbers

    // Start from the smallest power and go up to the point where the power is still <= n
    let current = 1;
    while (current ** x <= n) {
        let power = current ** x;
        for (let i = n; i >= power; i--) {
            dp[i] += dp[i - power];
        }
        current++;
    }

    return dp[n];
}
console.log(numberOfWays(10, 2));