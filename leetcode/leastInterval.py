from typing import List
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        hashTable = {}
        for s in tasks:
            if s not in hashTable:
                hashTable[s] = 1
            else:
                hashTable[s] += 1
        
        