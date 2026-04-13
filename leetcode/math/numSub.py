class Solution:
    def numSub(self, s: str) -> int:
        mod = 10**9 + 7
        i = 0
        n = len(s)
        res = 0
        while i < n:
            if s[i] == "1":
                start = i
                while s[i] == "1":
                    i += 1
                    if i == n:
                        break
                sub = i - start
                res += (sub + 1) * sub // 2
            i += 1
        return res % mod

             