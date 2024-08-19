function maximumLength(s: string): number {
    let freqMap = new Map<string, Map<number, number>>();
    let currChar = '';
    let currLen = 0;
    for (let i = 0; i < s.length; i++) {
        if (!freqMap.has(s[i])) {
            freqMap.set(s[i], new Map<number, number>());
            freqMap.get(s[i])!.set(1, 1);
            currChar = s[i];
            currLen = 1;
        } else {
            if (s[i] === currChar) {
                currLen++;
                freqMap.get(s[i])!.set(currLen, (freqMap.get(s[i])!.get(currLen) || 0) + 1);
            } else {
                currChar = s[i];
                currLen = 1;
                freqMap.get(s[i])!.set(currLen, (freqMap.get(s[i])!.get(currLen) || 0) + 1);
            }
        }
    }
    let maxLen = 0;
    for (let [key, value] of freqMap) {
        for (let [len, freq] of value) {
            if (freq >= 3) {
                maxLen = Math.max(maxLen, len);
            }
        }
    }
    return maxLen;
};