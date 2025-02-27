from typing import List
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        s = set(arr)
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                a, b = arr[i], arr[j]
                l = 2
                while a+b in s:
                    a, b = b, a+b
                    l += 1
                ans = max(ans, l)
        return ans if ans > 2 else 0