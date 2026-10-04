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

    # Recursive DFS, marks visited in place (no visited matrix)
    # Time O(R * C), Space O(R * C) recursion stack worst case
    # Note: mutates grid; LeetCode grid is strings '1'/'0', so marker is '-1'
    def numIslandsRecursive(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                # If a land cell is found, perform DFS to explore the full
                # island, and include this island in our count.
                if grid[r][c] == '1':
                    self.dfs(r, c, grid)
                    count += 1
        return count

    def dfs(self, r: int, c: int, grid: List[List[str]]) -> None:
        # Mark the current land cell as visited.
        grid[r][c] = '-1'
        # Define direction vectors for up, down, left, and right.
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        # Recursively call DFS on each neighboring land cell to continue
        # exploring this island.
        for d in dirs:
            next_r, next_c = r + d[0], c + d[1]
            if (self.is_within_bounds(next_r, next_c, grid)
                    and grid[next_r][next_c] == '1'):
                self.dfs(next_r, next_c, grid)

    def is_within_bounds(self, r: int, c: int, grid: List[List[str]]) -> bool:
        return 0 <= r < len(grid) and 0 <= c < len(grid[0])

    # Iterative version of numIslandsRecursive: explicit stack, marks in place
    # Time O(R * C), Space O(R * C) stack worst case — no recursion limit
    # Note: mutates grid
    def numIslandsIterative(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        count = 0
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != '1':
                    continue
                count += 1
                # Mark on push so a cell is never added to the stack twice.
                grid[r][c] = '-1'
                stack = [(r, c)]
                while stack:
                    cr, cc = stack.pop()
                    for d in dirs:
                        next_r, next_c = cr + d[0], cc + d[1]
                        if (self.is_within_bounds(next_r, next_c, grid)
                                and grid[next_r][next_c] == '1'):
                            grid[next_r][next_c] = '-1'
                            stack.append((next_r, next_c))
        return count


if __name__ == "__main__":
    def make():
        return [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
    s = Solution()
    assert s.numIslands(make()) == 3
    for f in (s.numIslandsRecursive, s.numIslandsIterative):
        assert f(make()) == 3
        assert f([["0"]]) == 0
        assert f([]) == 0
    # all-land grid: iterative handles it, recursive would hit RecursionError
    assert s.numIslandsIterative([["1"] * 300 for _ in range(300)]) == 1
    print("ok")