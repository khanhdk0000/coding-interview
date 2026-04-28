"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
"""

from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numMap = {}
        res = 0
        for n in nums:
            if n not in numMap:
                left = 0 if (n-1) not in numMap else numMap[n-1]
                right = 0 if (n+1) not in numMap else numMap[n+1]
                total = left + right + 1
                numMap[n] = total
                res = max(res, total)
                numMap[n-left] = total
                numMap[n+right] = total
            print(numMap)
        return res
    
    def longestConsecutive2(self, nums: List[int]) -> int:
        nums_set = set(nums)
        result = 0
        for num in nums_set:
            if num - 1 not in nums_set:
                current_num = num
                current_sequence = 1
                while current_num + 1 in nums_set:
                    current_sequence += 1
                    current_num += 1
                result = max(current_sequence, result)
        return result 



nums = [100,4,200,1,3,2]
nums = [0,3,7,2,5,8,4,6,0,1]

sol = Solution()


print(sol.longestConsecutive(nums))

