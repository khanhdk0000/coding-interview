from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_zero, col_zero = set(), set()
        # populate zero sets
        row_len, col_len = len(matrix), len(matrix[0])
        for r in range(row_len):
            for c in range(col_len):
                if matrix[r][c] == 0:
                    row_zero.add(r)
                    col_zero.add(c)
        
        for r in range(row_len):
            for c in range(col_len):
                if r in row_zero or c in col_zero:
                    matrix[r][c] = 0
