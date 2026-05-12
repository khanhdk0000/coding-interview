class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_map = {}
        res = 0
        left, right = 0, 0
        while right < len(s):
            if s[right] in s_map and (s_map[s[right]] >= left):
                left = s_map[s[right]] + 1
            s_map[s[right]] = right
            res = max(res, right - left + 1)
            print(left, right)
            right += 1
        return res