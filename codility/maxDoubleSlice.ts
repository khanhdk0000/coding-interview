function maxDoubleSlice(A: number[]): number {
    const n = A.length;

    // Arrays to store maximum sums up to and from each index
    const leftMax = new Array(n).fill(0);
    const rightMax = new Array(n).fill(0);

    // Calculate leftMax
    for (let i = 1; i < n - 1; i++) {
        leftMax[i] = Math.max(0, leftMax[i - 1] + A[i]);
    }

    // Calculate rightMax
    for (let i = n - 2; i > 0; i--) {
        rightMax[i] = Math.max(0, rightMax[i + 1] + A[i]);
    }

    // Calculate the maximum double slice sum
    let maxSum = 0;
    for (let i = 1; i < n - 1; i++) {
        maxSum = Math.max(maxSum, leftMax[i - 1] + rightMax[i + 1]);
    }

    return maxSum;
}
