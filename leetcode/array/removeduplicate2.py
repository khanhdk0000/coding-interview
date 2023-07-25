from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        j = 1
        prev = nums[0]
        isTwo = False
        while j < len(nums):
            if nums[j] == prev:
                if isTwo:
                    nums[j] = -101
                else:
                    isTwo = True
                # nums.pop(j)
            else:
                prev = nums[j]
                isTwo = False
            j += 1
        
        c = nums.count(-101)
        for i in range(c):  
            nums.remove(-101)
        return len(nums)
    
input = [1,1,1,2,2,3]
sol = Solution()
print(input, sol.removeDuplicates(input))