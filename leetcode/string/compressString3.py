class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        current = word[0]
        currentCount = 1
        maxCount = 9
        for i in range(1, len(word)):
            if word[i] == current:
                if currentCount == maxCount:
                    comp += str(currentCount) + current
                    current = word[i]
                    currentCount = 1
                else:
                    currentCount += 1
            else:
                comp += str(currentCount) + current
                current = word[i]
                currentCount = 1
        
        comp += str(currentCount) + current
        return comp

sol = Solution()
print(sol.compressedString("abcde")) 
print(sol.compressedString("aaaaaaaaaaaaaabb")) 