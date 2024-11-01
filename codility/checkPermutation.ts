function checkPermutation(A: number[]): number {
    // antisum
    const N = A.length;
    
    // Calculate the expected sum for a permutation of length N
    const expectedSum = (N * (N + 1)) / 2;

    // Calculate the actual sum of elements in A and use a Set to track duplicates
    const actualSum = A.reduce((acc, num) => acc + num, 0);
    const uniqueElements = new Set(A);

    // Check if actual sum matches expected sum and if there are no duplicates
    if (actualSum === expectedSum && uniqueElements.size === N) {
        return 1;
    } else {
        return 0;
    }
}
