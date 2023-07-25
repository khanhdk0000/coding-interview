from typing import List,  Optional
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = self.bfs(grid)
        flat_list = [item for sublist in grid for item in sublist]
        print(flat_list)
        if 1 in flat_list:
            return -1
        return minutes

    def bfs(self, grid):
        maxY = len(grid)    
        maxX = len(grid[0])
        queue = []
        coord = (0,0)
        queue.append(coord)
        rotten = False
        res = 0
        visited = []
        visited.append(coord)
        while queue:
            tmp = queue.pop(0)
            y, x = tmp[0], tmp[1]
            # move left
            if x < maxX-1:
                adj = (y, x + 1)
                if adj not in visited:
                    queue.append(adj)
                    visited.append(adj)
                if grid[y][x+1] == 1 and grid[y][x] == 2: 
                    grid[y][x+1] = 2
                    rotten = True
            # move right
            if x > 0:
                adj = (y, x - 1)
                if adj not in visited:
                    queue.append(adj)
                    visited.append(adj)
                if grid[y][x-1] == 1 and grid[y][x] == 2: 
                    grid[y][x-1] = 2
                    rotten = True
            # move up
            if y > 0:
                adj = (y - 1, x)
                if adj not in visited:
                    queue.append(adj)
                    visited.append(adj)
                if grid[y-1][x] == 1 and grid[y][x] == 2:    
                    grid[y-1][x] = 2
                    rotten = True
            # move down
            if y < maxY-1:
                adj = (y + 1, x)
                if adj not in visited:
                    queue.append(adj)
                    visited.append(adj)
                if grid[y+1][x] == 1 and grid[y][x] == 2: 
                    grid[y+1][x] = 2
                    rotten = True
            if rotten:
                res += 1
                rotten = False

        return res

sol = Solution()
input = [
    [2,0,1,1,1,1,1,1,1,1],
    [1,0,1,0,0,0,0,0,0,1],
    [1,0,1,0,1,1,1,1,0,1],
    [1,0,1,0,1,0,0,1,0,1],
    [1,0,1,0,1,0,0,1,0,1],
    [1,0,1,0,1,1,0,1,0,1],
    [1,0,1,0,0,0,0,1,0,1],
    [1,0,1,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1]]


print(sol.orangesRotting(input))


