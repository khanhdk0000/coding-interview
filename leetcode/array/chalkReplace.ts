function chalkReplacer(chalk: number[], k: number): number {
    const total = chalk.reduce((acc, curr) => acc + curr, 0);
    k %= total;
    let i = 0;
    while (k >= 0) {
        k -= chalk[i];
        i++;
    }
    return i - 1;
};