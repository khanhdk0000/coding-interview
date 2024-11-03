function commonPrimeDivisors(A: number[], B: number[]): number {
    // Step 1: Helper function to find the greatest common divisor
    const gcd = (a: number, b: number): number => {
        if (a % b === 0) {
            return b;
        }
        return gcd(b, a % b);
    };

    // Step 2: Helper function to check if two numbers have the same prime divisors
    const hasSamePrimeDivisors = (a: number, b: number): boolean => {
        const commonGcd = gcd(a, b);
        let gcdA = 0;
        let gcdB = 0;

        while (gcdA !== 1) {
            gcdA = gcd(a, commonGcd);
            a /= gcdA;
        }

        while (gcdB !== 1) {
            gcdB = gcd(b, commonGcd);
            b /= gcdB;
        }

        return a === 1 && b === 1;
    };

    // Step 3: Count the number of pairs with the same prime divisors
    let count = 0;
    for (let i = 0; i < A.length; i++) {
        if (hasSamePrimeDivisors(A[i], B[i])) {
            count++;
        }
    }

    return count;
}