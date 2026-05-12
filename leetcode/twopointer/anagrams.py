from collections import Counter
from typing import List


# Time Complexity: O(n) where n = len(s)
#   - Building p_count is O(k), k = len(p)
#   - The sliding window iterates over s once: O(n)
#   - Each step updates s_count and adjusts `matches` in O(1)
#   - No full dict comparison needed — just check matches == len(p_count)
#
# Space Complexity: O(1) — both dicts hold at most 26 keys (lowercase letters)
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_s, len_t = len(s), len(p)
        if len_t > len_s:
            return []
        res = []
        expected_freqs, window_freqs = [0] * 26, [0] * 26
        # Populate 'expected_freqs' with the characters in string 't'.
        for c in p:
            expected_freqs[ord(c) - ord('a')] += 1
        left = right = 0
        while right < len_s:
            # Add the character at the right pointer to 'window_freqs'
            # before sliding the window.
            window_freqs[ord(s[right]) - ord('a')] += 1
            # If the window has reached the expected fixed length, we
            # advance the left pointer as well as the right pointer to
            # slide the window.
            if right - left + 1 == len_t:
                if window_freqs == expected_freqs:
                    res.append(left)
                # Remove the character at the left pointer from
                # 'window_freqs' before advancing the left pointer.
                window_freqs[ord(s[left]) - ord('a')] -= 1
                left += 1
            right += 1
        return res
