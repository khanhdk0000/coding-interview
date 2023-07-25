class Solution:
    def longestPalindrome(self, words) -> int:
        res = 0
        hashTable = {}
        resDebug = []
        for w in words:
            if w in hashTable:
                res += 4
                resDebug.append(w)
                if hashTable[w] == 1:
                    hashTable.pop(w, None)
                else:
                    hashTable[w] -= 1
            else:
                if w[::-1] not in hashTable:
                    hashTable[w[::-1]] = 1
                else:
                    hashTable[w[::-1]] += 1
        for key in hashTable:
            if key[0] == key[1]:
                res += 2
                resDebug.append(key)
                break
        print(resDebug)
        return res
        
sol = Solution()
input = ["qo","fo","fq","qf","fo","ff","qq","qf","of","of","oo","of","of","qf","qf","of"]

print(sol.longestPalindrome(input))