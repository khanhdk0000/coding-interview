from typing import List
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        doubleMap = {}
        for num in arr:
            if num in doubleMap:
                return True
            doubleMap[num * 2] = num
            if num % 2 == 0:
                doubleMap[num // 2] = num
        return False

sol = Solution()
print(sol.checkIfExist([10,2,5,3]))
print(sol.checkIfExist([3,1,7,11]))