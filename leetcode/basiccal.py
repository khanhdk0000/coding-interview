from typing import List,  Optional, DefaultDict

class Solution:

    def __init__(self) -> None:
        self.highOp = ["*", "/"]
        self.Op = ["*", "/", "+", "-"]

    def calculate(self, s: str) -> int:
        stackPost = self.infixToPostfix(s)
        stack = []
        while stackPost:
            c = stackPost.pop(0)
            if c.isdigit():
                stack.append(int(c))
            else:
                first = stack.pop()
                second = stack.pop()
                stack.append(self.cal(first, second, c))
        return int(stack.pop())
                
    def cal(self, first: int, second: int, op: str) -> int:
        if op == "*":
            return first * second
        elif op == "/":
            return second // first
        elif op == "-":
            return second - first
        elif op == "+":
            return first + second


    def notGreaterPrecedence(self, stack, s: str) -> bool:
        priority = 0
        if s in self.highOp:
            priority = 1
        if stack[-1] in self.highOp and priority <= 1:
            return True
        if stack[-1] not in self.highOp and priority == 0:
            return True
        return False

    def infixToPostfix(self, s: str) -> List:
        stack = []
        stackRes = []
        tmp = ""
        for c in s:
            if c.isdigit():
                tmp += c
            elif c in self.Op:
                stackRes.append(tmp)
                tmp = ""
                while(len(stack) > 0 and self.notGreaterPrecedence(stack, c)):
                    stackRes.append(stack.pop())
                stack.append(c)

        if tmp != "":
            stackRes.append(tmp)

        while stack:
            stackRes.append(stack.pop())
        return stackRes
    

sol = Solution()
input = "2*3+4"
print(sol.infixToPostfix(input))
print(sol.calculate(input))

