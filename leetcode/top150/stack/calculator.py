class Solution:
    def calculate(self, s: str) -> int:
        # digits and +, -, (, ), " "
        stack = []
        num = 0
        sign = 1
        res = 0
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == "+":
                res += sign * num
                num = 0
                sign = 1
            elif c == "-":
                res += sign * num
                num = 0
                sign = -1
            elif c == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif c == ")":
                res += sign * num
                num = 0
                # sign
                res *= stack.pop()
                res += stack.pop()
        res += sign * num
        return res