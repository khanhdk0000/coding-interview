function minAvgSliceIndex(A: number[]): number {
    let minAvg = Infinity;
    let minIndex = 0;

    for (let i = 0; i < A.length - 1; i++) {
        // Calculate the 2-element slice average (i, i+1)
        const avg2 = (A[i] + A[i + 1]) / 2;
        if (avg2 < minAvg) {
            minAvg = avg2;
            minIndex = i;
        }

        // Calculate the 3-element slice average (i, i+1, i+2), if within bounds
        if (i < A.length - 2) {
            const avg3 = (A[i] + A[i + 1] + A[i + 2]) / 3;
            if (avg3 < minAvg) {
                minAvg = avg3;
                minIndex = i;
            }
        }
    }

    return minIndex;
}
