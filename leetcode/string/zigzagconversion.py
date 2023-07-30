"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
         
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
"""


from typing import List
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [""] * numRows if numRows > 1 else [""]
        i, step = 0, 1
        for c in s:
            rows[i] += c
            if numRows == 1:
                continue
            if i == 0:
                step = 1
            elif i == numRows - 1:
                step = -1
            i += step
        return "".join(rows)


s = "PAYPALISHIRING"
numRows = 3
numRows = 4
s = "ABC"
numRows = 1

sol = Solution()

print(sol.convert(s, numRows))