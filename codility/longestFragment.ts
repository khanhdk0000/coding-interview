function longestConsistentFragment(A: number[]): number {
    // Longest fraction contains at most 2 different digits
    // So we can use a sliding window to find the longest fragment
    let longestFragment = 0;
    let windowStart = 0;
    const digitsCount = new Map<number, number>();
    for (let windowEnd = 0; windowEnd < A.length; windowEnd++) {
        const digits = getDigits(A[windowEnd]);

        for (const d of digits) {
            digitsCount.set(d, (digitsCount.get(d) || 0) + 1);
        }

        while (digitsCount.size > 2) {
            const leftDigits = getDigits(A[windowStart]);

            for (const d of leftDigits) {
                const count = digitsCount.get(d)! - 1;
                if (count === 0) {
                    digitsCount.delete(d);
                } else {
                    digitsCount.set(d, count);
                }
            }
            windowStart += 1; 
        }

        longestFragment = Math.max(longestFragment, windowEnd - windowStart + 1);
    }
    return longestFragment;
}

function getDigits(n: number): number[] {
    const digits = new Set<number>();
    if (n === 0) {
        digits.add(0);
    } else {
        while (n > 0) {
            digits.add(n % 10);
            n = Math.floor(n / 10);
        }
    }
    return Array.from(digits);
}
