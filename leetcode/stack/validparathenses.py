"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

from typing import List
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openPara = {"{": "}", "[": "]", "(": ")"}
        for c in s:
            # print(stack)
            if c in openPara:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                topStack = stack.pop()
                if openPara[topStack] != c:
                    return False
        return True if len(stack) == 0 else False



s = "()"
s = "()[]{}"
s = "(]"
s = "([)]"
sol = Solution()


print(sol.isValid(s))

