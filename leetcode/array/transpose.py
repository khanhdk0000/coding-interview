from typing import List

# LeetCode 867 — Transpose Matrix
#
# Transpose: flip matrix over its diagonal → res[i][j] = matrix[j][i]
#
# ⚠️  WHY [[0]*m] * n IS WRONG:
#   `[0]*m` creates one list, then `* n` copies the REFERENCE n times.
#   All n rows point to the exact same list object in memory, so writing
#   res[0][1] = 5 also changes res[1][1], res[2][1], etc.
#
#   Fix: use a list comprehension — each iteration creates a NEW list:
#   [[0]*m for _ in range(n)]
#
# Time  : O(m * n)  — visit every cell exactly once
# Space : O(m * n)  — the output matrix (not counted as extra in LC)


class Solution:
    # ─────────────────────────────────────────────
    # Approach 1: Explicit index swap (most readable)
    # ─────────────────────────────────────────────
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)  # rows of input  = cols of output
        n = len(matrix[0])  # cols of input  = rows of output

        # ✅ Correct: list comprehension creates a fresh list per row
        res = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                res[i][j] = matrix[j][i]

        return res

    # ─────────────────────────────────────────────
    # Approach 2: Pythonic one-liner using zip
    # zip(*matrix) groups the i-th element of every row together,
    # which is exactly the i-th column → becomes the i-th row of transpose.
    # map(list, ...) converts each zip tuple into a list.
    # ─────────────────────────────────────────────
    def transpose_pythonic(self, matrix: List[List[int]]) -> List[List[int]]:
        return list(map(list, zip(*matrix)))
