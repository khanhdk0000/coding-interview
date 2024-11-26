from typing import List
class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        in_degree = [0] * n  # Step 1: Initialize in-degree array
        
        # Step 2: Compute in-degrees
        for u, v in edges:
            in_degree[v] += 1  # Team v is weaker than team u
        
        # Step 3: Identify teams with in-degree zero
        champions = [i for i in range(n) if in_degree[i] == 0]
        
        # Step 4: Determine if there is a unique champion
        if len(champions) == 1:
            return champions[0]  # Return the champion team
        else:
            return -1  # No unique champion
        
sol = Solution()
print(sol.findChampion(3, [[0,1],[1,2]]))
print(sol.findChampion(4, [[0,2],[1,3],[1,2]]))