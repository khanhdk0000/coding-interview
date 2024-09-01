function construct2DArray(original: number[], m: number, n: number): number[][] {
    if (original.length !== m * n) return [];

    const res: number[][] = [];
    for (let i = 0; i < m; i++) {
        res.push(original.slice(i * n, i * n + n));
    }

    return res;
};