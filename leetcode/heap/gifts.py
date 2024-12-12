from typing import List
import heapq
import math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = []
        for gift in gifts:
            heapq.heappush(heap, -gift)
            
        while k > 0:
            gift = -heapq.heappop(heap)
            heapq.heappush(heap, -math.floor(math.sqrt(gift)))
            k -= 1

        return -sum(heap)

sol = Solution()
# print(sol.pickGifts([25,64,9,4,100], 4))
# print(sol.pickGifts([1,1,1,1], 4))
print(sol.pickGifts([56,41,27,71,62,57,67,34,8,71,2,12,52,1,64,43,32,42,9,25,73,29,31], 52))