from typing import List
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        firstStr = s[:k]
        vowels = ['a', 'i', 'o', 'u', 'e']
        res = 0
        for i in firstStr:
            if i in vowels:
                res += 1
        if res == k:
            return k
        
        totalVow = res
        for i in range(k, len(s)):
            if res == k:
                return k
            firstChar = s[i - k]
            nexChar = s[i]
            if firstChar in vowels:
                totalVow -= 1
            if nexChar in vowels:
                totalVow += 1
            res = max(res, totalVow)
        return res

sol = Solution()
s = "leetcode"
k = 3
print(sol.maxVowels(s, k))
