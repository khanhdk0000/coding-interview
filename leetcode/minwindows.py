from typing import List,  Optional, DefaultDict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mapT = DefaultDict(int)
        for c in t:
            mapT[c] += 1
        
        res = ""
        start, end, sizeT = 0, 0, len(t)

        for end in range(len(s)):
            if mapT[s[end]] > 0:
                sizeT -= 1
            mapT[s[end]] -= 1

            while sizeT == 0:
                if res == "" or (end - start + 1) < len(res):
                    res = s[start:end+1]

                mapT[s[start]] += 1
                
                if mapT[s[start]] > 0:
                    sizeT += 1
                    
                start+=1

        return res

sol = Solution()
# input = [4,0,5,-5,3,3,0,-4,-5]
# print(sol.findFirstExist("DOBEC", "ABC"))
print(sol.minWindow("ADOBECODEBANC", "ABC"))