"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
"""


from typing import List
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1
        left, right = 0, len(needle) - 1
        while right <= len(haystack)-1:
            if haystack[left] == needle[0] and haystack[right] == needle[-1]:
                j = 1
                found = True
                # print(left, right)
                for i in range(left + 1, right):
                    if haystack[i] != needle[j]:
                        found = False
                        break
                    j += 1
                if found:
                    return left
            left += 1
            right += 1
        return -1



haystack = "sadbutsad"
needle = "sad"
haystack = "mississippi"
needle = "sippi"
haystack = "a"
needle = "a"
haystack = "mississippi"
needle = "sipp"

sol = Solution()

print(sol.strStr(haystack, needle))
