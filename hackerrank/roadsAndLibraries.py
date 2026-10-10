from typing import List


def roadsAndLibraries(n: int, c_lib: int, c_road: int, cities: List[List[int]]) -> int:
    # Library cheaper (or equal) than a road: put a library in every city.
    if c_lib <= c_road:
        return n * c_lib

    # Union-Find: each successful union = one road we actually need.
    parent = list(range(n + 1))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]  # path halving
            x = parent[x]
        return x

    roads = 0
    for a, b in cities:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb
            roads += 1

    # Every merge removes one component, so components = n - roads.
    # Each component: 1 library + (size - 1) roads.
    return (n - roads) * c_lib + roads * c_road


if __name__ == '__main__':
    assert roadsAndLibraries(8, 3, 2, [[1, 7], [1, 3], [1, 2], [2, 3], [5, 6], [6, 8]]) == 19  # city 4 isolated: 3 libs + 5 roads
    assert roadsAndLibraries(3, 2, 1, [[1, 2], [3, 1], [2, 3]]) == 4
    assert roadsAndLibraries(6, 2, 5, [[1, 3], [3, 4], [2, 4], [1, 2], [2, 3], [5, 6]]) == 12
    assert roadsAndLibraries(5, 6, 1, []) == 30  # no roads: every city alone
    print("ok")
