class Solution:
    def minWindow(self, s: str, t: str) -> str:
        charMap = {}
        for c in t:
            charMap[c] = charMap.get(c, 0) + 1
        left = 0
        right = 0
        res = ""
        minLen = float('inf')
        count = len(t)
        while right < len(s):
            c = s[right]
            if c in charMap:
                charMap[c] -= 1
                if charMap[c] >= 0:
                    count -= 1
            while count == 0:
                if right - left + 1 < minLen:
                    minLen = right - left + 1
                    res = s[left:right+1]
                c = s[left]
                if c in charMap:
                    charMap[c] += 1
                    if charMap[c] > 0:
                        count += 1
                left += 1
            right += 1
        return res