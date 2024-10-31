function minDifference(A: number[]): number {
    const n = A.length;
    const sum = A.reduce((acc, val) => acc + val, 0);
    let minDiff = Number.MAX_SAFE_INTEGER;
    let leftSum = 0;
    for (let i = 0; i < n - 1; i++) {
        leftSum += A[i];
        const rightSum = sum - leftSum;
        const diff = Math.abs(leftSum - rightSum);
        minDiff = Math.min(minDiff, diff);
    }
    return minDiff;
}