function missingRolls(rolls: number[], mean: number, n: number): number[] {
    const m = rolls.length;
    const sum = mean * (m + n);
    const sumRolls = rolls.reduce((acc, curr) => acc + curr, 0);
    const sumMissing = sum - sumRolls;
    // Maximum each dice is 6
    if (sumMissing < n || sumMissing > 6 * n) {
        return [];
    }
    const avg = Math.floor(sumMissing / n);
    const remain = sumMissing % n;
    const res = new Array(n).fill(avg);
    for (let i = 0; i < remain; i++) {
        res[i]++;
    }
    return res;
};