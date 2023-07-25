from typing import List,  Optional

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.rows = len(heights)
        self.cols = len(heights[0])
        res = []

        for i in range(self.rows):
            for j in range(self.cols):
                coord = [i, j]
                if(self.dfs(heights, coord)):
                    res.append(coord)
        return res
            
    def dfs(self, heights, coord):
        stack = []
        visited = []
        stack.append(coord)
        pacific, atlantic = False, False
        while stack:
            x, y = stack.pop()
            visited.append([x, y])
            if x == 0 or y == 0:
                pacific = True
            if x == self.rows - 1 or y == self.cols - 1:
                atlantic = True
            if pacific and atlantic:
                return True
            for dx, dy in [(1,0), (-1, 0), (0,1), (0,-1)]:
                xx = x + dx
                yy = y + dy
                if xx < 0 or xx == self.rows or yy < 0 or yy == self.cols:
                    continue
                if heights[x][y] < heights[xx][yy]:
                    continue
                if [xx, yy] not in visited:
                    stack.append([xx, yy])
        return False


sol = Solution()
input = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]


print(sol.pacificAtlantic(input))
