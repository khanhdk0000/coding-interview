from typing import List
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        
        # Step 1: Find the non-decreasing prefix
        left = 0
        while left + 1 < n and arr[left] <= arr[left + 1]:
            left += 1
            
        # If the whole array is non-decreasing
        if left == n - 1:
            return 0
        
        # Step 1: Find the non-decreasing suffix
        right = n - 1
        while right > 0 and arr[right - 1] <= arr[right]:
            right -= 1
        
        # Step 2: Initialize the answer
        ans = min(n - left - 1, right)
        
        # Step 3: Try to merge prefix and suffix
        i = 0
        j = right
        while i <= left and j < n:
            if arr[i] <= arr[j]:
                # Update the minimum length to remove
                ans = min(ans, j - i - 1)
                i += 1
            else:
                # Move the suffix pointer to find a larger or equal value
                j += 1
        
        return ans

sol = Solution()
print(sol.findLengthOfShortestSubarray([1,2,3,10,4,2,3,5])) # 3