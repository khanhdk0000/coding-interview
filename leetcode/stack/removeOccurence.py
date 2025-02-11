class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        for c in s:
            stack.append(c)
            if len(stack) >= len(part) and ''.join(stack[-len(part):]) == part:
                for _ in range(len(part)):
                    stack.pop()
        return ''.join(stack)
    
sol = Solution()
print(sol.removeOccurrences("daabcbaabcbc", "abc")) 
print(sol.removeOccurrences("axxxxyyyyb", "xy")) 