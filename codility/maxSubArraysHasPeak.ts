function maxBlocksWithPeak(A: number[]): number {
    const n = A.length;

    // Step 1: Identify all peaks
    const peaks: number[] = [];
    for (let i = 1; i < n - 1; i++) {
        if (A[i] > A[i - 1] && A[i] > A[i + 1]) {
            peaks.push(i);
        }
    }

    const numPeaks = peaks.length;
    if (numPeaks === 0) return 0;

    // Step 2: Check all divisors of N to find the maximum K
    for (let K = numPeaks; K >= 1; K--) {
        if (n % K !== 0) continue; // K must be a divisor of N

        const blockSize = n / K;
        let peakFound = new Array(K).fill(false);
        let peakBlocks = 0;

        // Step 3: Mark blocks that contain peaks
        for (const peak of peaks) {
            const blockIndex = Math.floor(peak / blockSize);
            if (!peakFound[blockIndex]) {
                peakFound[blockIndex] = true;
                peakBlocks++;
            }
        }

        // If every block has at least one peak, return K
        if (peakBlocks === K) {
            return K;
        }
    }

    return 0;
}
