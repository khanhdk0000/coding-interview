from typing import List
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rowMap, res = {}, 0
        for row in grid:
            rowString = ','.join(str(i) for i in row)
            if rowString not in rowMap:
                rowMap[rowString] = 0
            rowMap[rowString] += 1

        transposed = [[0 for j in range(len(grid))] for i in range(len(grid))]

        # Invert the rows and columns
        for i in range(len(grid)):
            for j in range(len(grid)):
                transposed[j][i] = grid[i][j]
        print(rowMap, transposed)
        for row in transposed:
            rowString = ','.join(str(i) for i in row)
            if rowString in rowMap:
                res += rowMap[rowString]
        return res

sol = Solution()
grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
str2 = "bca"
print(sol.equalPairs(grid))