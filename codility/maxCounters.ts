function maxCounters(N: number, A: number[]): number[] {
    const counters = new Array(N).fill(0);
    let maxCounter = 0;  // Track the maximum value of any counter
    let currentMax = 0;  // Track the last applied max counter value

    for (const operation of A) {
        if (operation >= 1 && operation <= N) {
            // Increase operation
            const index = operation - 1;
            
            // Apply lazy maxCounter update to the specific counter if needed
            if (counters[index] < currentMax) {
                counters[index] = currentMax;
            }

            // Increase the counter
            counters[index] += 1;

            // Update the maxCounter if this counter exceeded it
            maxCounter = Math.max(maxCounter, counters[index]);
        } else if (operation === N + 1) {
            // Max Counter operation
            currentMax = maxCounter;
        }
    }

    // Final pass to set all counters to at least currentMax
    for (let i = 0; i < N; i++) {
        if (counters[i] < currentMax) {
            counters[i] = currentMax;
        }
    }

    return counters;
}