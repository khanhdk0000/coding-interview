function DNASequence(S: string, P: number[], Q: number[]): number[] {
    const n = S.length;
    const m = P.length;
    const result: number[] = new Array(m);

    // Initialize prefix sums for each nucleotide
    const A = new Array(n + 1).fill(0);
    const C = new Array(n + 1).fill(0);
    const G = new Array(n + 1).fill(0);
    const T = new Array(n + 1).fill(0);

    // Build prefix sums
    for (let i = 0; i < n; i++) {
        // Carry over previous counts
        A[i + 1] = A[i];
        C[i + 1] = C[i];
        G[i + 1] = G[i];
        T[i + 1] = T[i];

        // Increment the count for the current nucleotide
        if (S[i] === 'A') A[i + 1]++;
        else if (S[i] === 'C') C[i + 1]++;
        else if (S[i] === 'G') G[i + 1]++;
        else if (S[i] === 'T') T[i + 1]++;
    }

    // Process each query
    for (let k = 0; k < m; k++) {
        const start = P[k];
        const end = Q[k] + 1; // Exclusive end in prefix sums

        // Check for the minimum impact factor in the range
        if (A[end] - A[start] > 0) {
            result[k] = 1; // A is present
        } else if (C[end] - C[start] > 0) {
            result[k] = 2; // C is present
        } else if (G[end] - G[start] > 0) {
            result[k] = 3; // G is present
        } else {
            result[k] = 4; // T is present
        }
    }

    return result;
}
