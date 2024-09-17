function uncommonFromSentences(s1: string, s2: string): string[] {
    const wordMap = new Map<string, number>();
    const words = s1.split(' ').concat(s2.split(' '));
    for (const word of words) {
        wordMap.set(word, (wordMap.get(word) || 0) + 1);
    }
    // return words that only appear once
    return Array.from(wordMap.entries()).filter(([word, count]) => count === 1).map(([word, count]) => word);
};