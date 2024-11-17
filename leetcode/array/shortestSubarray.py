from typing import List
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        
        res = -1
        q = []
        for i in range(n + 1):
            while q and prefix[i] - prefix[q[0]] >= k:
                res = i - q.pop(0) if res == -1 else min(res, i - q.pop(0))
            while q and prefix[i] <= prefix[q[-1]]:
                q.pop()
            q.append(i)
        return res
    
s = Solution()
print(s.shortestSubarray([1], 1))
print(s.shortestSubarray([1,2], 4))
print(s.shortestSubarray([2,-1,2], 3))
print(s.shortestSubarray([84,-37,32,40,95], 167))
print(s.shortestSubarray([-28,81,-20,28,-29], 89))