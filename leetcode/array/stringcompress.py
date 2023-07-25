from typing import List
class Solution:
    def compress(self, chars: List[str]) -> int:
        c, count = chars[0], 1
        s = ""
        for i in range(1, len(chars)):
            if chars[i] == c:
                count += 1
            else:
                s += c + str(count) if count > 1 else c
                c = chars[i]
                count = 1
        s += c + str(count) if count > 1 else c
        for i in range(len(s)):
            chars[i] = s[i]
        print(chars, len(s))
        if len(chars) > len(s):
            del chars[len(s):]
            # print(chars)
        print(chars, len(s))
        return s
        
sol = Solution()
chars = ["a"]
# ["a","3","b","2","c","3"]
print(sol.compress(chars))
print(chars)