from typing import List
import heapq
class Solution:

    def digitSum(self, num: int) -> int:
        return sum([int(x) for x in str(num)])

    def maximumSum(self, nums: List[int]) -> int:
        groups = {}
        for num in nums:
            sumDigits = self.digitSum(num)
            if sumDigits not in groups:
                groups[sumDigits] = []
                heapq.heappush(groups[sumDigits], -num)
            else:
                heapq.heappush(groups[sumDigits], -num)
        maxSum = -1
        for key, value in groups.items():
            if len(value) > 1:
                value1 = int(-heapq.heappop(value))
                value2 = int(-heapq.heappop(value))
                pairSum = value1 + value2
                maxSum = max(maxSum, pairSum)
        return maxSum
    
sol = Solution()
# print(sol.maximumSum([18,43,36,13,7]))
# print(sol.maximumSum([10,12,19,14]))
print(sol.maximumSum([229,398,269,317,420,464,491,218,439,153,482,169,411,93,147,50,347,210,251,366,401]))