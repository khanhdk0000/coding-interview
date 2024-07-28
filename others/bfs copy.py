import heapq
from collections import deque, defaultdict
import sys

def find_min(arr):
    # Select the unvisited vertex with the smallest distance
    min_vertex = None
    min_distance = sys.maxsize
    min_path = []
    index = 0
    for idx, ele in enumerate(arr):
        current_cost, current_vertex, path = ele
        if current_cost < min_distance:
            min_vertex = current_vertex
            min_distance = current_cost
            min_path = path
            index = idx
    return min_vertex, min_distance, min_path, index


def bfs_shortest_path(v, adjacency_matrix, start, goal):
    pq = [(0, start, [start])]  # path cost, vertex, path
    parent: {
        ten dinh = <tap phan tu dinh,path>
    }

    parent<string,list>
    queue = [start]

    # Visited set to keep track of visited vertices
    visited = set()
    visited.add(start)

A -> B, C,D
B-> E

e,...
a,b,c,d
    while queue:
        node = queue.pop(0): B
        for neighbor in range(v): E
            weight != 0 and neighbor not in visited
            queue.append(neighbor)
            visited.add(neighbor)
            parent[neighbor] = [parent[B], neighbor]->
           
        

        
        
    


        current_vertex, current_cost, path, index = find_min(pq)
        pq.pop(index)
        # print(current_cost, current_vertex, path)
        if current_vertex == goal:
            return path, len(visited), current_cost
        
        
    return "Not Found", len(visited), 0

def main():
    input = """6 1
W K I U M Q
0	0	0	0	4	2
0	0	0	0	0	0
3	4	0	4	3	0
7	7	0	0	0	6
0	0	0	6	0	4
0	0	8	0	1	0
U I"""
    data = input.strip().split('\n')
    
    v, n = map(int, data[0].split())
    vertices = data[1].split()
    index = {vertices[i]: i for i in range(len(vertices))}

    adjacency_matrix = []
    for i in range(2, 2 + v):
        adjacency_matrix.append(list(map(int, data[i].split())))
    # print(adjacency_matrix, data)
    results = []
    for i in range(2 + v, 2 + v + n):
        start, goal = data[i].split()
        start_index, goal_index = index[start], index[goal]
        path, count, length = bfs_shortest_path(v, adjacency_matrix, start_index, goal_index)
        if path == "Not Found":
            results.append("Not Found\n0 0")
        else:
            path = ' '.join(vertices[j] for j in path)
            results.append(f"{path}\n{count} {length}")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
