function numJewelsInStones(jewels: string, stones: string): number {
    const jewelMap = new Map<string, number>();
    for (let i = 0; i < jewels.length; i++) {
        jewelMap.set(jewels[i], 0);
    }
    let count = 0;
    for (let i = 0; i < stones.length; i++) {
        if (jewelMap.has(stones[i])) {
            count++;
        }
    }
    return count;
};