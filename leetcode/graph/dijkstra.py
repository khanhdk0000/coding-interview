import heapq

def dijkstra(graph, start):
    """
    Computes the shortest paths from the start node to all other nodes in the graph.

    :param graph: A dictionary where keys are node identifiers and values are lists of tuples
                  (neighbor, weight) representing the edges and their weights.
    :param start: The starting node identifier.
    :return: A dictionary mapping nodes to their shortest distance from the start node.
    """
    # Initialize the priority queue with the start node and distance 0
    heap = [(0, start)]
    # Initialize all distances to infinity
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    # Set to keep track of visited nodes
    visited = set()

    while heap:
        current_distance, current_node = heapq.heappop(heap)

        # Skip if we've already visited this node
        if current_node in visited:
            continue

        visited.add(current_node)

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            # If a shorter path to neighbor is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances

# Example usage:
if __name__ == "__main__":
    # Define the graph as an adjacency list
    graph = {
        'A': [('B', 5), ('C', 1)],
        'B': [('A', 5), ('C', 2), ('D', 1)],
        'C': [('A', 1), ('B', 2), ('D', 4), ('E', 8)],
        'D': [('B', 1), ('C', 4), ('E', 3), ('F', 6)],
        'E': [('C', 8), ('D', 3)],
        'F': [('D', 6)]
    }

    start_node = 'A'
    shortest_distances = dijkstra(graph, start_node)
    print(f"Shortest distances from node {start_node}:")
    for node, distance in shortest_distances.items():
        print(f"Distance to {node}: {distance}")
