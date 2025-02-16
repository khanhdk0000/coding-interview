class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        n = len(needle)
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                if haystack[i:i+n] == needle:
                    return i
        return -1
    
sol = Solution()
print(sol.strStr("mississippi", "issip")) 