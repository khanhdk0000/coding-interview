from typing import List


class Solution:
    # 695. Max Area of Island
    # Same DFS as numberOfIslands.py, but count cells per island
    # Time O(R * C), Space O(R * C)
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        max_area = 0

        def dfs(r, c):
            # iterative, returns island size
            area = 0
            stack = [(r, c)]
            while stack:
                x, y = stack.pop()
                if x < 0 or x >= rows or y < 0 or y >= cols or visited[x][y] or grid[x][y] == 0:
                    continue
                visited[x][y] = True
                area += 1
                # add all 4 directions
                stack.append((x + 1, y))
                stack.append((x - 1, y))
                stack.append((x, y + 1))
                stack.append((x, y - 1))
            return area

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and not visited[i][j]:
                    max_area = max(max_area, dfs(i, j))

        return max_area

    # Iterative DFS, marks visited in place (no visited matrix)
    # Time O(R * C), Space O(R * C) stack worst case
    # Note: mutates grid; 695 grid is ints, so marker is -1
    def maxAreaOfIslandIterative(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        max_area = 0
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != 1:
                    continue
                # Mark on push so a cell is never added to the stack twice.
                grid[r][c] = -1
                area = 1
                stack = [(r, c)]
                while stack:
                    r1, c1 = stack.pop()
                    for d in dirs:
                        nxt_r, nxt_c = r1 + d[0], c1 + d[1]
                        if 0 <= nxt_r < len(grid) and 0 <= nxt_c < len(grid[0]) and grid[nxt_r][nxt_c] == 1:
                            grid[nxt_r][nxt_c] = -1
                            area += 1
                            stack.append((nxt_r, nxt_c))
                max_area = max(max_area, area)
        return max_area


if __name__ == "__main__":
    grid = [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    ]
    s = Solution()
    for f in (s.maxAreaOfIsland, s.maxAreaOfIslandIterative):
        assert f([row[:] for row in grid]) == 6  # copy: iterative mutates grid
        assert f([[0, 0, 0, 0, 0, 0, 0, 0]]) == 0
        assert f([[1]]) == 1
        assert f([]) == 0
    print("ok")
