from typing import List
'''
Use Boyer-Moore Majority Voting Algorithm
Time complexity O(n)
Space complexity O(1)
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        votes = 0
        candidate = -1
        for n in nums:
            if votes == 0:
                candidate = n
                votes += 1
            elif n == candidate:
                votes += 1
            else:
                votes -= 1

        return candidate

input = [3,3,4]
sol = Solution()
print(input, sol.majorityElement(input))