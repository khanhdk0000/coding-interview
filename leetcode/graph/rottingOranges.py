from collections import deque
from typing import List


class Solution:
    # 994. Rotting Oranges
    # Multi-source BFS: all rotten oranges start in the queue as level 0,
    # each BFS level = 1 minute
    # Time O(R * C), Space O(R * C)
    # Note: mutates grid
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = deque()
        ones = seconds = 0
        # Count the total number of fresh oranges and add each rotten
        # orange to the queue to represent level 0 of the level-order traversal.
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    ones += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))
        # Use level-order traversal to determine how long it takes to
        # rot the fresh oranges.
        while queue and ones > 0:
            # 1 minute passes with each level of the grid that's explored.
            seconds += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                # Rot any neighboring fresh oranges and add them to the queue
                # to be processed in the next level.
                for d in dirs:
                    next_r, next_c = r + d[0], c + d[1]
                    if (self.is_within_bounds(next_r, next_c, grid)
                            and grid[next_r][next_c] == 1):
                        grid[next_r][next_c] = 2
                        ones -= 1
                        queue.append((next_r, next_c))
        # If there are still fresh oranges left, return -1. Otherwise,
        # return the time passed.
        return seconds if ones == 0 else -1

    def is_within_bounds(self, r: int, c: int, grid: List[List[int]]) -> bool:
        return 0 <= r < len(grid) and 0 <= c < len(grid[0])


if __name__ == "__main__":
    s = Solution()
    assert s.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4
    assert s.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1
    assert s.orangesRotting([[0, 2]]) == 0
    assert s.orangesRotting([[0]]) == 0
    assert s.orangesRotting([[1]]) == -1
    print("ok")
