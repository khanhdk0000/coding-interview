from typing import List
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        sum = 0
        numMap = {}
        for i in range(k):
            if nums[i] in numMap:
                numMap[nums[i]] += 1
            else:
                numMap[nums[i]] = 1
            sum += nums[i]
        
            
        left = 0
        right = k -1
        maxSum = 0
        if len(numMap.keys()) == k:
            maxSum = sum
        while right < len(nums) - 1:
            numMap[nums[left]] -= 1
            if numMap[nums[left]] == 0:
                numMap.pop(nums[left])
            sum -= nums[left]
            left += 1
            right += 1
            if nums[right] in numMap:
                numMap[nums[right]] += 1
            else:
                numMap[nums[right]] = 1
            sum += nums[right]
            if len(numMap.keys()) == k:
                maxSum = max(maxSum, sum)
        
        return maxSum

sol = Solution()
print(sol.maximumSubarraySum([1,5,4,2,9,9,9], 3))
print(sol.maximumSubarraySum([4,4,4], 3))
print(sol.maximumSubarraySum([1,1,1,7,8,9], 3))