from typing import List

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # Flatten the board to a string
        start = ''.join(str(num) for row in board for num in row)
        target = '123450'
        
        # Define the neighbors for each position in the flattened board
        neighbors = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4],
        }
        
        # Initialize BFS variables
        queue = []
        queue.append((start, 0))
        visited = set()
        visited.add(start)
        
        while queue:
            state, moves = queue.pop(0)
            if state == target:
                return moves
            zero_index = state.index('0')
            for neighbor in neighbors[zero_index]:
                new_state = list(state)
                # Swap the zero with the neighbor
                new_state[zero_index], new_state[neighbor] = new_state[neighbor], new_state[zero_index]
                new_state_str = ''.join(new_state)
                if new_state_str not in visited:
                    visited.add(new_state_str)
                    queue.append((new_state_str, moves + 1))
        # If the target state is not reachable
        return -1

sol = Solution()
print(sol.slidingPuzzle([[1,2,3],[4,0,5]])) # 1 
print(sol.slidingPuzzle([[1,2,3],[5,4,0]])) 
print(sol.slidingPuzzle([[4,1,2],[5,0,3]])) 