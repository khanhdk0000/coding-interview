function arrayRotation(A: number[], K: number): number[] {
    // Implement your solution here
    if (K > A.length) {
        K = K % A.length;
    }
    const sliceIndex = A.length - K;
    const firstSlice = A.slice(0, sliceIndex);
    const secondSlice = A.slice(sliceIndex);
    return [...secondSlice, ...firstSlice];
}
