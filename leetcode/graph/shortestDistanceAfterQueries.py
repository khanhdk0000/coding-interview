from typing import List

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # Initialize the graph with the initial unidirectional roads
        graph = [[] for _ in range(n)]
        for i in range(n - 1):
            graph[i].append(i + 1)

        answer = []

        # Process each query
        for query in queries:
            u, v = query
            # Add the new road to the graph
            graph[u].append(v)

            # Perform BFS to find the shortest path from 0 to n - 1
            shortest_distance = self.bfs(graph, n)

            # Append the result to the answer list
            answer.append(shortest_distance)

        return answer

    def bfs(self, graph: List[List[int]], n: int) -> int:
        # Initialize the queue for BFS and the visited list
        queue = []
        queue.append((0, 0))  # (current_node, current_distance)
        visited = [False] * n
        visited[0] = True

        while queue:
            current_node, current_distance = queue.pop(0)

            # If we reach the destination, return the distance
            if current_node == n - 1:
                return current_distance

            # Explore neighbors
            for neighbor in graph[current_node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append((neighbor, current_distance + 1))

        # If n - 1 is not reachable, return -1 or a large number as per requirement
        return -1  # Assuming there is always a path as per problem constraints

        


sol = Solution()
print(sol.shortestDistanceAfterQueries(5, [[2,4],[0,2],[0,4]]))
# print(sol.shortestDistanceAfterQueries(4, [[0,3],[0,2]]))
# print(sol.shortestDistanceAfterQueries(8, [[5,7],[0,6]]))