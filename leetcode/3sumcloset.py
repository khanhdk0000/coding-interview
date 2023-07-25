from typing import List,  Optional
import sys
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) == 3:
            return sum(nums)
        nums.sort()
        res = sys.maxsize
        for first in range(len(nums)-2):
            second, third= first + 1, len(nums)-1
            while second < third:
                temSum = nums[first] + nums[second] + nums[third]
                if temSum == target:
                    return temSum
                if temSum < target:
                    second += 1
                elif temSum > target:
                    third -= 1
                if abs(temSum - target) < abs(res - target):
                    res = temSum
        return res
            

    
sol = Solution()
input = [4,0,5,-5,3,3,0,-4,-5]


print(sol.threeSumClosest(input, -2))
        