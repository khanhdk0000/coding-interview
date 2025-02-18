from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        res = []
        rowBegin, rowEnd = 0, len(matrix)-1
        colBegin, colEnd = 0, len(matrix[0])-1
        total = len(matrix) * len(matrix[0])
        while rowBegin <= rowEnd and colBegin <= colEnd:
            # go left
            for i in range(colBegin, colEnd + 1):
                res.append(matrix[rowBegin][i])
            rowBegin += 1
            if len(res) == total:
                break
            # go down
            for i in range(rowBegin, rowEnd + 1):
                res.append(matrix[i][colEnd])
            colEnd -= 1
            if len(res) == total:
                break
            # go right
            for i in range(colEnd, colBegin - 1, -1):
                res.append(matrix[rowEnd][i])
            rowEnd -= 1
            if len(res) == total:
                break
            # go up
            for i in range(rowEnd, rowBegin -1, -1):
                res.append(matrix[i][colBegin])
            colBegin += 1
            if len(res) == total:
                break
        return res

sol = Solution()
print(sol.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))