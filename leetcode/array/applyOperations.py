from typing import List
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        for i in range(n):
            res[i] = nums[i]
        for i in range(n-1):
            if res[i] == res[i+1]:
                res[i] = 2 * res[i]
                res[i+1] = 0
        j = 0
        for i in range(n):
            if res[i] != 0:
                res[j] = res[i]
                j += 1
        while j < n:
            res[j] = 0
            j += 1
        return res