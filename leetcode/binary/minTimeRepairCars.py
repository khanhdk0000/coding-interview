import math
from typing import List

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        # Helper function: can we repair all 'cars' within time 't'?
        def canFixAll(t: int) -> bool:
            total_fixed = 0
            for r in ranks:
                # max cars a mechanic with rank r can fix in time t:
                # n = floor(sqrt(t / r))
                n = int(math.isqrt(t // r))  # or math.floor((t / r)**0.5)
                total_fixed += n
                if total_fixed >= cars:  # no need to keep summing if we already meet the target
                    return True
            return False
        
        # Binary search boundaries
        left = 0
        # A safe upper bound: best rank * cars^2
        # because worst-case, a single best-rank mechanic fixes all cars
        best_rank = min(ranks)
        right = best_rank * (cars**2)
        
        # Binary search
        while left < right:
            mid = (left + right) // 2
            if canFixAll(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
