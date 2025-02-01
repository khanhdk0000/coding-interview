class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) == 0 or len(nums) == 1:
            return True
        for i in range(len(nums)-1):
            if nums[i] % 2 == 0 and nums[i+1] % 2 == 0:
                return False
            if nums[i] % 2 == 1 and nums[i+1] % 2 == 1:
                return False
        return True