from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    # 133. Clone Graph
    # DFS + hash map original -> clone (map also acts as visited set, handles cycles)
    # Time O(V + E), Space O(V)
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        # fresh map per call — a mutable default `clone_map = {}` would be shared
        # across calls and return stale clones from a previous graph
        return self.dfs(node, {})

    def dfs(self, node: 'Node', clone_map: dict) -> 'Node':
        # If this node was already cloned, then return this previously cloned node.
        if node in clone_map:
            return clone_map[node]
        # Clone the current node.
        cloned_node = Node(node.val)
        # Store the current clone to ensure it doesn't need to be created
        # again in future DFS calls.
        clone_map[node] = cloned_node
        # Iterate through the neighbors of the current node to connect
        # their clones to the current cloned node.
        for neighbor in node.neighbors:
            cloned_neighbor = self.dfs(neighbor, clone_map)
            cloned_node.neighbors.append(cloned_neighbor)
        return cloned_node

    # Iterative DFS with explicit stack — no recursion depth limit
    # Time O(V + E), Space O(V)
    def cloneGraphIterative(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        # Clone the start node and remember it.
        w
        stack = [node]
        while stack:
            curr = stack.pop()
            for neighbor in curr.neighbors:
                # First time seeing this neighbor: clone it and visit it later.
                if neighbor not in clone_map:
                    clone_map[neighbor] = Node(neighbor.val)
                    stack.append(neighbor)
                # Connect the neighbor's clone to the current node's clone.
                clone_map[curr].neighbors.append(clone_map[neighbor])
        return clone_map[node]


def build(adj):
    nodes = [Node(i + 1) for i in range(len(adj))]
    for i, nbrs in enumerate(adj):
        nodes[i].neighbors = [nodes[j - 1] for j in nbrs]
    return nodes[0] if nodes else None


def to_adj(node):
    # BFS back to adjacency list, checking clone shares no nodes with original
    seen, order, i = {node.val: node}, [node], 0
    while i < len(order):
        for n in order[i].neighbors:
            if n.val not in seen:
                seen[n.val] = n
                order.append(n)
        i += 1
    return seen, [[n.val for n in seen[v].neighbors] for v in sorted(seen)]


if __name__ == "__main__":
    adj = [[2, 4], [1, 3], [2, 4], [1, 3]]
    s = Solution()
    for f in (s.cloneGraph, s.cloneGraphIterative):
        for _ in range(2):  # run twice: catches shared-state bugs between calls
            original = build(adj)
            clone = f(original)
            orig_nodes, _ = to_adj(original)
            clone_nodes, clone_adj = to_adj(clone)
            assert clone_adj == adj
            assert all(clone_nodes[v] is not orig_nodes[v] for v in orig_nodes)
        assert f(None) is None
        single = f(Node(1))
        assert single.val == 1 and single.neighbors == []
    print("ok")
