from typing import List
import heapq
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heap = []
        operations = 0
        for num in nums:
            heapq.heappush(heap, num)
        
        while len(heap) > 1:
            smallest = heapq.heappop(heap)
            secondSmallest = heapq.heappop(heap)
            if smallest >= k:
                break
            newNum = smallest*2 + secondSmallest
            heapq.heappush(heap, newNum)
            operations += 1
        return operations

sol = Solution()
print(sol.minOperations([2,11,10,1,3], 10)) 
print(sol.minOperations([1,1,2,4,9], 20)) 
