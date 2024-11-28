from collections import deque
from typing import List

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
        deque_q = deque([(0, 0, 0)])  # (cost, x, y), start with cost 0 at (0, 0)
        visited = [[False] * n for _ in range(m)]  # To track visited nodes
        
        while deque_q:
            cost, x, y = deque_q.popleft()
            
            if (x, y) == (m - 1, n - 1):  # Reached bottom-right corner
                return cost
            
            if visited[x][y]:
                continue
            visited[x][y] = True
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    if grid[nx][ny] == 0:  # No obstacle
                        deque_q.appendleft((cost, nx, ny))  # Add to front
                    else:  # Obstacle
                        deque_q.append((cost + 1, nx, ny))  # Add to back
        
        return -1  # If no path is found (though problem guarantees a path)

sol = Solution()
print(sol.minimumObstacles([[0,1,1],[1,1,0],[1,1,0]])) 
print(sol.minimumObstacles([[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]])) 