function maximumNumberOfStringPairs(words: string[]): number {
    let map = new Map<string, number>();
    let count = 0;
    for (let i = 0; i < words.length; i++) {
        let sortedWord = words[i].split("").sort().join("");
        if (map.has(sortedWord)) {
            count++;
            map.delete(sortedWord);
        } else {
            map.set(sortedWord, 1);
        }
    }
    return count;
};