class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for char in s:
            if char.isdigit():
                if stack:
                    stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)
    
sol = Solution()
print(sol.clearDigits("abc"))
print(sol.clearDigits("cb34"))