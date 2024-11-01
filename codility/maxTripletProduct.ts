function maxTripletProduct(A: number[]): number {
    const n = A.length;
    A.sort((a, b) => a - b);
    
    return Math.max(A[n - 1] * A[n - 2] * A[n - 3], A[0] * A[1] * A[n - 1]);
}