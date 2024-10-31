function earliestFrogJump(X: number, A: number[]): number {
    const n = A.length;
    const leaves = new Set();
    for (let i = 0; i < n; i++) {
        leaves.add(A[i]);
        if (leaves.size === X) {
            return i;
        }
    }
    return -1;
}