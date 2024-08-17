function maxPoints(points: number[][]): number {
    let m = points.length, n = points[0].length;
    
    // Initialize dp array with the values of the first row
    let dp = points[0].slice();

    for (let i = 1; i < m; i++) {
        // Arrays to hold the best scores from left to right and right to left
        let leftToRight = new Array(n).fill(-Infinity);
        let rightToLeft = new Array(n).fill(-Infinity);
        let newDp = new Array(n).fill(-Infinity);

        // Calculate from left to right
        leftToRight[0] = dp[0];
        for (let j = 1; j < n; j++) {
            leftToRight[j] = Math.max(leftToRight[j - 1] - 1, dp[j]);
        }

        // Calculate from right to left
        rightToLeft[n - 1] = dp[n - 1];
        for (let j = n - 2; j >= 0; j--) {
            rightToLeft[j] = Math.max(rightToLeft[j + 1] - 1, dp[j]);
        }

        // Update dp array for the current row
        for (let j = 0; j < n; j++) {
            newDp[j] = Math.max(leftToRight[j], rightToLeft[j]) + points[i][j];
        }

        // Transfer newDp to dp for the next iteration
        dp = newDp;
    }

    // Return the maximum value in the dp array
    return Math.max(...dp);

};