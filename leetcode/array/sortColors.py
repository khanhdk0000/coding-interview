class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        numsMap = {
            0: 0,
            1: 0,
            2: 0,
        }
        for n in nums:
            if n in numsMap:
                numsMap[n] += 1
        
        idx = 0
        for key, value in numsMap.items():
            for i in range(value):
                nums[idx]= key
                idx += 1
        