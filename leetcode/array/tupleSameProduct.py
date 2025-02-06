from typing import List
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 4:
            return 0
        count = 0
        product = {}
        for i in range(n):
            for j in range(i+1, n):
                p = nums[i] * nums[j]
                count += product.get(p, 0)
                product[p] = product.get(p, 0) + 1
        return count * 8

sol = Solution()
print(sol.tupleSameProduct([2,3,4,6]))
print(sol.tupleSameProduct([1,2,4,5,10]))

