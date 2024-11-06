class Solution:
    def minChanges(self, s: str) -> int:
        changes = 0
        n = len(s)
        for i in range(0, n, 2):
            if s[i] != s[i + 1]:
                changes += 1
        return changes
    

sol = Solution()
print(sol.minChanges("1001"))
print(sol.minChanges("10"))
print(sol.minChanges("0000"))
print(sol.minChanges("11000111"))