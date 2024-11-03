function nonDivisors(A: number[]): number[] {
    const n = A.length;

    // Step 1: Create a frequency map
    const frequencyMap: Map<number, number> = new Map();
    for (const num of A) {
        frequencyMap.set(num, (frequencyMap.get(num) || 0) + 1);
    }

    // Step 2: Calculate divisors count for each unique number
    const divisorCount: Map<number, number> = new Map();
    for (const [x, freq] of frequencyMap.entries()) {
        let count = 0;
        for (let d = 1; d * d <= x; d++) {
            if (x % d === 0) {
                // d is a divisor
                count += frequencyMap.get(d) || 0;
                // x / d is also a divisor (if different)
                if (d !== x / d) {
                    count += frequencyMap.get(x / d) || 0;
                }
            }
        }
        divisorCount.set(x, count);
    }

    // Step 3: Calculate non-divisors for each element in A
    return A.map(num => n - (divisorCount.get(num) || 0));
}
