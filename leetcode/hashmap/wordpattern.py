"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false

"""

from typing import List
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        patternMap, sMap = {}, {}
        sList = s.split()
        if len(sList) != len(pattern):
            return False
        for idx, val in enumerate(pattern):
            if val not in patternMap:
                if sList[idx] in sMap:
                    return False
                patternMap[val] = sList[idx]
                sMap[sList[idx]] = val
            else:
                if patternMap[val] != sList[idx]:
                    return False
        return True


pattern = "abba"
s = "dog cat cat dog"
# s = "dog cat cat fish"
pattern = "abba"
s = "dog dog dog dog"
sol = Solution()


print(sol.wordPattern(pattern, s))

