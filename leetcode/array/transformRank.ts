function arrayRankTransform(arr: number[]): number[] {
    const sortedArr = [...arr].sort((a, b) => a - b);
    const rankMap = new Map();
    let rank = 1;
    for (const num of sortedArr) {
        if (!rankMap.has(num)) {
            rankMap.set(num, rank++);
        }
    }
    return arr.map(num => rankMap.get(num)!);
};