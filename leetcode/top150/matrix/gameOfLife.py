from typing import List
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 0: dead, 1: live
        # Live with < 2 live neighbors -> dead
        # Live with 2 or 3 live neighbors -> live
        # Live with > 3 live neighbors -> dead
        # Dead with 3 live neighbors -> live
        if not board:
            return
        m = len(board)
        n = len(board[0])
        liveMatrix = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                liveNeighbors = self.countLiveNeighbors(board, i, j)
                liveMatrix[i][j] = liveNeighbors
        for i in range(m):
            for j in range(n):
                if board[i][j] == 1 and (liveMatrix[i][j] < 2 or liveMatrix[i][j] > 3):
                    board[i][j] = 0
                if board[i][j] == 0 and liveMatrix[i][j] == 3:
                    board[i][j] = 1
    
    def countLiveNeighbors(self, board: List[List[int]], i: int, j: int) -> int:
        m, n = len(board), len(board[0])
        count = 0
        for x in range(max(0, i-1), min(m, i+2)):
            for y in range(max(0, j-1), min(n, j+2)):
                count += board[x][y]
        if board[i][j] == 1:
            count -= 1
        return count
    
sol = Solution()
board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
sol.gameOfLife(board)
print(board)