from typing import List,  Optional
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = []
        def dfs(p):
            for i, j in enumerate(isConnected[p]):
                if j == 1 and i not in visited:
                    visited.append(i)
                    dfs(i)

        res = 0
        for i in range(len(isConnected)):
            if i not in visited:
                res += 1
                visited.append(i)
                dfs(i)
        return res