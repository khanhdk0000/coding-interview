from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        res, j = 1, 1
        prev = nums[0]
        while j < len(nums):
            if nums[j] == prev:
                nums[j] = -101
                # nums.pop(j)
            else:
                prev = nums[j]
                res += 1
            j += 1
        c = nums.count(-101)
        for i in range(c):  
            nums.remove(-101)
        # nums = [el for el in nums if el != -101]
        return res
    
input = [0,0,1,1,1,2,2,3,3,4]
sol = Solution()
print(input, sol.removeDuplicates(input))