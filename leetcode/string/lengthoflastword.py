"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal 
substring
 consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
"""


from typing import List
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i, res, findLastWord = len(s) - 1, 0, False
        while i >= 0:
            if s[i] != " ":
                findLastWord = True
                res += 1
            elif s[i] == " ":
                if findLastWord:
                    return res
            i -= 1
        return res




s = "Hello World"
# s = "   fly me   to   the moon  "
s = "luffy is still joyboy"

sol = Solution()

print(sol.lengthOfLastWord(s))