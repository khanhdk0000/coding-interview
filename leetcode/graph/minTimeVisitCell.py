from typing import List
import heapq

class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # Edge case: Check if we can move from the starting cell
        if m > 1 and grid[1][0] > 1 and n > 1 and grid[0][1] > 1:
            return -1
        if m == 1 and n > 1 and grid[0][1] > 1:
            return -1
        if n == 1 and m > 1 and grid[1][0] > 1:
            return -1

        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = 0
        heap = [(0, 0, 0)]  # (time, row, col)

        while heap:
            t, i, j = heapq.heappop(heap)

            # If we have reached the destination
            if i == m - 1 and j == n - 1:
                return t

            # Skip if we have found a better path already
            if t > dist[i][j]:
                continue

            for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    if grid[ni][nj] <= t + 1:
                        t_prime = t + 1
                    else:
                        t_prime = grid[ni][nj]
                        if (t_prime - t) % 2 == 0:
                            t_prime += 1

                    if t_prime < dist[ni][nj]:
                        dist[ni][nj] = t_prime
                        heapq.heappush(heap, (t_prime, ni, nj))

        # If the destination is unreachable
        return -1

    
sol = Solution()
print(sol.minimumTime([[0,1,3,2],[5,1,2,5],[4,3,8,6]]))
print(sol.minimumTime([[0,2,4],[3,2,1],[1,0,4]]))