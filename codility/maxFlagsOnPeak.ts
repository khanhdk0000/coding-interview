function maxFlagsOnPeak(A: number[]): number {
    const n = A.length;

    // Step 1: Find all peaks
    const peaks: number[] = [];
    for (let i = 1; i < n - 1; i++) {
        if (A[i] > A[i - 1] && A[i] > A[i + 1]) {
            peaks.push(i);
        }
    }

    const numPeaks = peaks.length;
    if (numPeaks === 0) return 0;

    // Step 2: Binary search for the maximum number of flags
    let left = 1;
    let right = numPeaks;
    let maxFlags = 0;

    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        
        // Check if we can place `mid` flags with distance of at least `mid`
        let usedFlags = 1;
        let lastFlagPosition = peaks[0];

        for (let i = 1; i < numPeaks; i++) {
            if (peaks[i] - lastFlagPosition >= mid) {
                usedFlags++;
                lastFlagPosition = peaks[i];
                if (usedFlags === mid) break;
            }
        }

        if (usedFlags >= mid) {
            maxFlags = mid;
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return maxFlags;
}
