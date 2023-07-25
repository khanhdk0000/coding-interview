from typing import List,  Optional
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if len(rooms[0]) == 0:
            return False
        visited = [0]
        keys = set(rooms[0])
        while keys:
            key = keys.pop()
            if key not in visited:
                visited.append(key)
                keys.update(rooms[key])
            else:
                continue
        return len(visited) == len(rooms)
