function solution(N: number, P: number[], Q: number[]): number[] {
    // Step 1: Sieve of Eratosthenes to find all primes up to N
    const isPrime = new Array(N + 1).fill(true);
    isPrime[0] = isPrime[1] = false;

    for (let i = 2; i * i <= N; i++) {
        if (isPrime[i]) {
            for (let j = i * i; j <= N; j += i) {
                isPrime[j] = false;
            }
        }
    }

    // Step 2: Generate semiprimes using primes
    const isSemiprime = new Array(N + 1).fill(0);

    for (let i = 2; i <= N; i++) {
        if (isPrime[i]) {
            for (let j = i; i * j <= N; j++) {
                if (isPrime[j]) {
                    isSemiprime[i * j] = 1;
                }
            }
        }
    }

    // Step 3: Prefix sum array to count semiprimes up to each index
    const semiprimeCount = new Array(N + 1).fill(0);
    for (let i = 1; i <= N; i++) {
        semiprimeCount[i] = semiprimeCount[i - 1] + isSemiprime[i];
    }

    // Step 4: Answer each query using the prefix sum array
    const result: number[] = [];
    for (let k = 0; k < P.length; k++) {
        result.push(semiprimeCount[Q[k]] - semiprimeCount[P[k] - 1]);
    }

    return result;
}
