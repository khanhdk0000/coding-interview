function maxSlice(A: number[]): number {
    // number can be negative
    if (A.length === 0) {
        return 0;
    }
    const n = A.length;
    let maxEnding = A[0];
    let maxSlice = A[0];
    for (let i = 1; i < n; i++) {
        maxEnding = Math.max(A[i], maxEnding + A[i]);
        maxSlice = Math.max(maxSlice, maxEnding);
    }
    return maxSlice;
}
