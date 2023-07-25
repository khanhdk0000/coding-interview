from typing import List,  Optional
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        existedCity = {}
        existedCity[0] = 1
        index = 0
        res = 0
        connections.sort(key= lambda x: x[0])
        # print(connections)
        while connections:
            city1, city2 = connections[index]
            # print(city1, city2, res)
            if city1 not in existedCity and city2 not in existedCity:
                index += 1
                continue
            if city1 in existedCity and city2 not in existedCity:
                res += 1
                existedCity[city2] = 1
            elif city1 not in existedCity and city2 in existedCity:
                existedCity[city1] = 1
            # print(res, len(connections))
            connections.pop(index)
            index = 0
        return res
    
    def sol2(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for u, v in connections:
            graph[u].append((v, 1))
            graph[v].append((u, 0))
            
        q = deque([0])
        visited = {0}
        res = 0
        
        while q:
            city = q.popleft()
            
            for neighbor, cost in graph[city]:
                if neighbor not in visited: 
                    visited.add(neighbor)
                    res += cost
                    q.append(neighbor)
                    
        return res
# input = [[0,1],[1,3],[2,3],[4,0],[4,5]]
input = [[4,3],[2,3],[1,2],[1,0]]
sol = Solution()
print(sol.minReorder(6, input))