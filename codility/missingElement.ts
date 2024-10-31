
function missingElement(A: number[]): number {
    const n = A.length + 1;
    const sum = (n * (n + 1)) / 2;
    const actualSum = A.reduce((acc, val) => acc + val, 0);
    return sum - actualSum;
}
