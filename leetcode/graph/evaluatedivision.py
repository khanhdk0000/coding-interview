from typing import List,  Optional
from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        numMap = defaultdict(list)
        for idx, eq in enumerate(equations):
            numMap[eq[0]].append((eq[1], values[idx]))
            numMap[eq[1]].append((eq[0], 1/values[idx]))

        res = [0] * len(queries)
        # print(numMap)

        def bfs(a, b):
            queue = [(a, 1)]
            visited = [a]
            while queue:
                num, value = queue.pop(0)
                if num not in numMap:
                    return -1
                if num == b:
                    return value
                for numVal in numMap[num]:
                    if numVal[0] not in visited:
                        visited.append(numVal[0])
                        queue.append((numVal[0], value * numVal[1]))
            return -1

        for idx, query in enumerate(queries):
            res[idx] = bfs(query[0], query[1])
        return res
    
equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
# queries = [["x","x"]]
sol = Solution()
print(sol.calcEquation(equations, values, queries))