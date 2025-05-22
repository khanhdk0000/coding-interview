from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        num_islands = 0

        def dfs(r, c):
            # iterative
            stack = [(r, c)]
            while stack:
                x, y = stack.pop()
                if x < 0 or x >= rows or y < 0 or y >= cols or visited[x][y] or grid[x][y] == '0':
                    continue
                visited[x][y] = True
                # add all 4 directions
                stack.append((x + 1, y))
                stack.append((x - 1, y))
                stack.append((x, y + 1))
                stack.append((x, y - 1))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and not visited[i][j]:
                    num_islands += 1
                    dfs(i, j)

        return num_islands