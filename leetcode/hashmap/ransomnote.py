"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
"""

from typing import List
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazineMap = {}
        for c in magazine:
            if c not in magazineMap:
                magazineMap[c] = 0
            magazineMap[c] += 1

        for c in ransomNote:
            if c not in magazineMap or magazineMap[c] == 0:
                return False
            magazineMap[c] -= 1
        return True
                


ransomNote = "a"
magazine = "b"
ransomNote = "aa"
magazine = "ab"
ransomNote = "aa"
magazine = "aab"
sol = Solution()


print(sol.canConstruct(ransomNote, magazine))

