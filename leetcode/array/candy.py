"""
problem 135
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

    + Each child must have at least one candy.
    + Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

Example 1:
Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

Example 2:
Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
"""
from typing import List
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candy = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candy[i] = candy[i-1] + 1

        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1] and candy[i] <= candy[i+1]:
                candy[i] = candy[i+1] + 1
        # print(candy)
        return sum(candy)


input = [1,2,2] # 4
input = [1,3,2,2,1] # 7 1,2,1,2,1
# input = [29,51,87,87,72,12] # 12
# input = [1,6,10,8,7,3,2] # 18
sol = Solution()

print(sol.candy(input))