
function NumberOfDiscIntersections(A: number[]): number {
    const n = A.length;
    const start: number[] = new Array(n);
    const end: number[] = new Array(n);

    // Populate start and end arrays
    for (let i = 0; i < n; i++) {
        start[i] = i - A[i];
        end[i] = i + A[i];
    }

    // Sort start and end arrays
    start.sort((a, b) => a - b);
    end.sort((a, b) => a - b);

    let intersections = 0;
    let activeDiscs = 0;
    let endIdx = 0;

    // Count intersections by iterating over the start array
    for (let i = 0; i < n; i++) {
        // For each start point, count how many discs are active
        while (endIdx < n && end[endIdx] < start[i]) {
            activeDiscs--; // Disc at endIdx ends before the current disc starts
            endIdx++;
        }

        intersections += activeDiscs;
        if (intersections > 10_000_000) return -1;

        activeDiscs++;
    }

    return intersections;
}