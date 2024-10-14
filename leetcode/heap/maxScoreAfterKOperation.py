import heapq
import math
class Solution(object):
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, -num)

        res = 0
        while k > 0:
            num = int(-heapq.heappop(heap))
            res += num
            heapq.heappush(heap, -math.ceil(num/3))
            k -= 1

        return res