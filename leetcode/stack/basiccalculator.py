"""
Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

Example 1:

Input: s = "1 + 1"
Output: 2
Example 2:

Input: s = " 2-1 + 2 "
Output: 3
Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
"""

from typing import List
import re
class Solution:
    def calculate(self, s: str) -> int:
        s = s.strip()
        sList = re.findall('[+-/*//()]|\d+',s)
        if len(s) == 0:
            return 0
        if s.isdigit():
            return int(s)
        stack, num = [], 0
        op = {"+": 0, "-": 0}
        for c in sList:
            # print(stack)
            if c == " ":
                continue
            if c == ")":
                while True:
                    num = stack.pop()
                    opOrNum = stack.pop()
                    if opOrNum in op:
                        nextNum = stack.pop()
                        if opOrNum == "+":
                            stack.append(str(int(nextNum) + int(num)))
                        elif opOrNum == "-":
                            stack.append(str(int(nextNum) - int(num)))
                    elif opOrNum == "(":
                        stack.append(num)
                        break
            elif c not in op and c != "(" and len(stack) > 0 and stack[-1] in op:
                operand = stack.pop()
                if len(stack) > 0 and stack[-1].lstrip('-+').isdigit():
                    num = int(stack.pop())
                    if operand == "+":
                        stack.append(str(int(c) + num))
                    elif operand == "-":
                        stack.append(str(num - int(c)))
                else:
                    if operand == "+":
                        stack.append(c)
                    elif operand == "-":
                        stack.append(str(int(c)*-1))
            else:
                stack.append(c)
        # print(stack)
        while len(stack) > 2:
            firstNum, operand, secondNum = stack.pop(0), stack.pop(0), stack.pop(0)
            if operand == "+":
                stack.insert(0, str(int(secondNum)+int(firstNum)))
            elif operand == "-":
                stack.insert(0, str(int(firstNum)-int(secondNum)))
        # print(stack)
        if len(stack) == 2:
            num, op = stack.pop(), stack.pop()
            if op == "-":
                stack.append(str(int(num)*-1))
            else:
                stack.append(num)
        return int(stack.pop())




s = "1 + 1"
s = " 2-1 + 2 "
# s = "(1+(4+5+2)-3)+(6+8)"
s = "2147483647"
s= "1-(     -2)"
s= "-2+ 1"
# s= "- (3 + (4 + 5))"
# s = "1-11"
# s = "(7)-(0)+(4)"
sol = Solution()

print(sol.calculate(s))

