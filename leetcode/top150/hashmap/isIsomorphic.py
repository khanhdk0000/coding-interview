class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sMap = {}
        tMap = {}
        for i in range(len(s)):
            if s[i] in sMap:
                if sMap[s[i]] != t[i]:
                    return False
            else:
                sMap[s[i]] = t[i]
            if t[i] in tMap:
                if tMap[t[i]] != s[i]:
                    return False
            else:
                tMap[t[i]] = s[i]
        return True