class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        length = len(s1) - 2
        for i in range(0, length):
            if s1[i] == s2[i] and s1[i+2] == s2[i+2]:
                continue
            if not (s1[i] == s2[i+2] and s1[i+2] == s2[i]):
                return False
        return True 