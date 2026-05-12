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
        if len(p) > len(s):
            return []

        p_count = Counter(p)
        s_count = Counter(s[: len(p)])

        # matches = number of characters whose counts agree in both windows
        matches = sum(s_count[c] == p_count[c] for c in p_count)
        res = [0] if matches == len(p_count) else []

        for i in range(len(p), len(s)):
            right_c = s[i]
            left_c = s[i - len(p)]

            # Add right character to window
            if p_count.get(right_c):
                if s_count[right_c] == p_count[right_c]:
                    matches -= 1  # was matching, now will be over
                s_count[right_c] += 1
                if s_count[right_c] == p_count[right_c]:
                    matches += 1  # now matches again

            # Remove left character from window
            if p_count.get(left_c):
                if s_count[left_c] == p_count[left_c]:
                    matches -= 1  # was matching, now will be under
                s_count[left_c] -= 1
                if s_count[left_c] == p_count[left_c]:
                    matches += 1  # now matches again

            if matches == len(p_count):
                res.append(i - len(p) + 1)

        return res
