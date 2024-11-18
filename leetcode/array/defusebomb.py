from typing import List
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        res = [0] * len(code)
        if k == 0:
            return res
        totalSum = sum(code[1: k+1]) if k > 0 else sum(code[k:])
        print(totalSum)
        res[0] = totalSum
        leftIndex = 1 if k > 0 else k
        rightIndex = k if k > 0 else -1
        for i in range(1, len(code)):
            totalSum -= code[leftIndex]
            leftIndex = (leftIndex + 1) % len(code) 
            rightIndex = (rightIndex + 1) % len(code)
            totalSum = totalSum + code[rightIndex]
            res[i] = totalSum
        return res
    
sol = Solution()
print(sol.decrypt([5,7,1,4], 3))
print(sol.decrypt([1,2,3,4], 0))
print(sol.decrypt([2,4,9,3], -2))