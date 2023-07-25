from typing import List

"""
time O(n)
space O(1)
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i, steps, n = 0, nums[0], len(nums) - 1
        while i < n:
            if steps == 0:
                if nums[i] == 0:
                    break
                else:
                    steps = nums[i]

            if nums[i+1] >= steps:
                steps = nums[i+1]
            else:
                steps -= 1
            i += 1
        return i == n 
            
            


input = [3,0,0,0]
sol = Solution()

print(sol.canJump(input))