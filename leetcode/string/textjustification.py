"""
Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
 

Example 1:

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:

Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.
Example 3:

Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
"""


from typing import List
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        arrWords = [[]]
        arrLen = [0]
        i, j = 0, 0
        while j < len(words):
            if len(words[j]) + arrLen[i] <= maxWidth:
                arrLen[i] += len(words[j]) + 1
                if len(arrWords[i]) == 0:
                    arrWords[i].append(words[j])
                else:
                    arrWords[i].append(" ")
                    arrWords[i].append(words[j])
                j += 1
            else:
                arrLen[i] -= 1
                i += 1
                arrWords.append([])
                arrLen.append(0)
        arrLen[-1] -= 1

        for i in range(len(arrWords)-1):
            numEle = len(arrWords[i])
            while arrLen[i] != maxWidth:
                if numEle == 1:
                    arrWords[i] += " "*(maxWidth-arrLen[i])
                    arrLen[i] = maxWidth
                    break
                for j in range(1, numEle, 2):
                    arrWords[i][j] += " "
                    arrLen[i] += 1
                    if arrLen[i] == maxWidth:
                        break
        if arrLen[-1] != maxWidth:
            arrWords[-1].append(" "*(maxWidth-arrLen[-1]))
        res = [""]*len(arrLen)
        for i in range(len(arrLen)):
            res[i] = "".join(arrWords[i])     
        return res


words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16

words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16

words= ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20

sol = Solution()

print(sol.fullJustify(words, maxWidth))
