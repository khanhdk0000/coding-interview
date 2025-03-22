from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # Build adjacency list
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = [False] * n
        complete_components_count = 0
        
        def bfs(start):
            queue = [start]
            visited[start] = True
            component_nodes = []
            
            # Standard BFS to collect all nodes in this connected component
            while queue:
                node = queue.pop()
                component_nodes.append(node)
                for neighbor in adj[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
            return component_nodes
        
        for i in range(n):
            if not visited[i]:
                # Get all nodes in this connected component
                comp_nodes = bfs(i)
                k = len(comp_nodes)  # number of vertices in the component
                
                # Count edges within this component
                edge_count = 0
                for node in comp_nodes:
                    edge_count += len(adj[node])
                edge_count //= 2  # each edge was counted twice (undirected)
                
                # Check if it forms a complete graph: 
                # A complete graph on k vertices should have k*(k-1)/2 edges
                if edge_count == (k * (k - 1)) // 2:
                    complete_components_count += 1
        
        return complete_components_count

    
sol = Solution()
# print(sol.countCompleteComponents(6, [[0,1],[0,2],[1,2],[3,4]]))
# print(sol.countCompleteComponents(6, [[0,1],[0,2],[1,2],[3,4],[3,5]]))
print(sol.countCompleteComponents(4, [[1,0],[2,0],[3,1],[3,2]]))