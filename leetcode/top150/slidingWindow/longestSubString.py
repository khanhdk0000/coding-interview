class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        maxLen = 0
        charMap = {}
        while right < len(s):
            if s[right] in charMap:
                left = max(left, charMap[s[right]] + 1)
            charMap[s[right]] = right
            maxLen = max(maxLen, right - left + 1)
            right += 1
        return maxLen