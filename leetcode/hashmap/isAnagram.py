"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
"""

from typing import List
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sMap = {}
        for c in s:
            if c not in sMap:
                sMap[c] = 0
            sMap[c] += 1
        
        for c in t:
            if c not in sMap or sMap[c] == 0:
                return False
            sMap[c] -= 1
        return True

s = "anagram"
t = "nagaram"
s = "rat"
t = "car"
sol = Solution()


print(sol.isAnagram(s, t))

