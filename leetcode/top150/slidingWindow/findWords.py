from typing import List
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wordLen = len(words[0])
        wordCount = len(words)
        wordMap = {}
        for word in words:
            wordMap[word] = wordMap.get(word, 0) + 1
        res = []
        totalLen = wordLen * wordCount
        
        for i in range(len(s) - totalLen + 1):
            seen = {}
            for j in range(i, i + totalLen, wordLen):
                word = s[j:j+wordLen]
                if word not in wordMap:
                    break
                seen[word] = seen.get(word, 0) + 1
                if seen[word] > wordMap[word]:
                    break
            if seen == wordMap:
                res.append(i)
        return res
    
sol = Solution()
print(sol.findSubstring("barfoothefoobarman", ["foo","bar"])) # [0,9]
print(sol.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"])) # [8]