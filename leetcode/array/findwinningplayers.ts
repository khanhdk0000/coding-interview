function findWinningPlayer(skills: number[], k: number): number {
    let currentIdx = 0;
    let currentCount = 0;
    for (let i = 1; i < skills.length; i++) {
        if (skills[i] > skills[currentIdx]) {
            currentIdx = i;
            currentCount = 0;
        }
        currentCount++;
        if (currentCount === k) {
            break;
        }
    }
    return currentIdx;
}
