"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
"""

from typing import List
class Solution:
    def asciiWord(self, word: str) -> int:
        return sum(ord(c) % 26 for c in word)


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaMap = {}
        for s in strs:
            sortVal = ''.join(sorted(s))
            if sortVal not in anaMap:
                anaMap[sortVal] = [s]
            else:
                anaMap[sortVal].append(s)
                
        return [lst for lst in anaMap.values()]



strs = ["eat","tea","tan","ate","nat","bat"]
strs = ["cab","tin","pew","duh","may","ill","buy","bar","max","doc"]
# [["max"],["buy"],["doc"],["may"],["ill"],["duh"],["tin"],["bar"],["pew"],["cab"]]
sol = Solution()

# print(sol.asciiWord("buy"))
# print(sol.asciiWord("doc"))

print(sol.groupAnagrams(strs))

