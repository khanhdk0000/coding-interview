from typing import List
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total = 0
        min_abs = float('inf')
        neg_count = 0
        for row in matrix:
            for num in row:
                total += abs(num)
                if num < 0:
                    neg_count += 1
                min_abs = min(min_abs, abs(num))
        if neg_count % 2 == 0:
            return total
        else:
            return total - 2 * min_abs

sol = Solution()
print(sol.maxMatrixSum([[1,-1],[-1,1]]))
print(sol.maxMatrixSum([[1,2,3],[-1,-2,-3],[1,2,3]]))