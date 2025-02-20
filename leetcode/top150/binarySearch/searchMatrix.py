from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # search for the target in the 2D matrix
        # binary search
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        # search column
        left, right = 0, m-1
        while left <= right:
            mid = left + (right - left) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1
        # search row
        row = right
        if row < 0:
            return False
        left, right = 0, n-1
        while left <= right:
            mid = left + (right - left) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
# Time: O(log(m) + log(n))