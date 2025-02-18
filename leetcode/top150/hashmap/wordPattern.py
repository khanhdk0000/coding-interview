class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        patternMap = {}
        sMap = {}
        for i, c in enumerate(pattern):
            if c not in patternMap:
                patternMap[c] = i
        sList = s.split()
        if len(pattern) != len(sList):
            return False
        for i, word in enumerate(sList):
            if word not in sMap:
                sMap[word] = i
            if patternMap[pattern[i]] != sMap[word]:
                return False
        return True