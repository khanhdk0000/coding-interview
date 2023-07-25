from typing import List
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        word1Map, word2Map, occur1Map, occur2Map = {},{},{},{}
        i, j, len1, len2 = 0, 0, len(word1), len(word2)
        while i < len1 or j < len2:
            if i < len1:
                if word1[i] not in word1Map:
                    word1Map[word1[i]] = 0
                word1Map[word1[i]] += 1
            if j < len2:
                if word2[j] not in word2Map:
                    word2Map[word2[j]] = 0
                word2Map[word2[j]]+= 1
            i+=1
            j+=1

        for c in word1:
            if c not in word2Map:
                return False
        for c in word2:
            if c not in word1Map:
                return False
            
        lst1 = list(word1Map.values())
        lst2 = list(word2Map.values())
        for c in word1:
            occur1 = word1Map[c]
            occur2 = word2Map[c]
            if occur1 == occur2:
                continue
            else:
                if occur2 not in lst1:
                    return False
                
        # number of each occurences must match
        for i in lst1:
            if i not in occur1Map:
                occur1Map[i] = 0
            occur1Map[i] += 1

        for i in lst2:
            if i not in occur2Map:
                occur2Map[i] = 0
            occur2Map[i] += 1

        # print(lst1, lst2, occur1Map, occur2Map)
        for oc1 in lst1:
            oc2 = occur2Map[oc1]
            if occur1Map[oc1] != oc2:
                return False

        return True 

sol = Solution()
str1 = "abc"
str2 = "bca"
print(sol.closeStrings(str1, str2))