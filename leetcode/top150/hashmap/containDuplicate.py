from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numsMap = {}
        for i, num in enumerate(nums):
            if num in numsMap and abs(i - numsMap[num]) <= k:
                return True
            numsMap[num] = i
        return False