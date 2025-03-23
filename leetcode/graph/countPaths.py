from typing import List
import heapq

MOD = 10**9 + 7

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        # Build adjacency list: graph[node] = [(neighbor, weight), ...]
        graph = [[] for _ in range(n)]
        for u, v, t in roads:
            graph[u].append((v, t))
            graph[v].append((u, t))

        # Distances array, initialized to infinity
        dist = [float('inf')] * n
        # Ways array, ways[i] = number of shortest paths from 0 to i
        ways = [0] * n

        # Distance to start node = 0, ways to start node = 1
        dist[0] = 0
        ways[0] = 1

        # Min-heap for Dijkstra (distance, node)
        pq = [(0, 0)]  # (distance so far, node)

        while pq:
            cur_dist, node = heapq.heappop(pq)
            
            # If this distance is stale, skip
            if cur_dist > dist[node]:
                continue

            # Explore neighbors
            for neighbor, time_cost in graph[node]:
                new_dist = cur_dist + time_cost

                # Found a shorter path to 'neighbor'
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    ways[neighbor] = ways[node]
                    heapq.heappush(pq, (new_dist, neighbor))
                
                # Found another path of the same (shortest) distance
                elif new_dist == dist[neighbor]:
                    ways[neighbor] = (ways[neighbor] + ways[node]) % MOD

        # Number of shortest ways to reach n-1
        return ways[n - 1] % MOD
