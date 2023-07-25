from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        forwardLst = [0]*(n-1)
        backwardLst = [0]*(n-1)

        forwardLst[0], backwardLst[0] = nums[0], nums[-1]
        first, last = 1, n - 2

        while first < n - 1 and last > 0:
            forwardLst[first] = forwardLst[first - 1] * nums[first]
            backwardLst[first] = backwardLst[first - 1] * nums[last]
            first += 1
            last -= 1
        print(forwardLst, backwardLst)

        res = [0] * n
        for i in range(n):
            if i == 0:
                res[i] = backwardLst[-1]
            elif i == n - 1:
                res[i] = forwardLst[-1]
            else:
                res[i] = forwardLst[i-1] * backwardLst[n - i - 2]
        return res


sol = Solution()
input = [-1,1,0,-3,3]

print(sol.productExceptSelf(input))