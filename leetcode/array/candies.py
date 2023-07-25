from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        largest = candies[0]
        for e in candies:
            if e > largest:
                largest = e

        res = [False] * len(candies)
        print(largest)

        for i in range(len(candies)):
            if candies[i] + extraCandies >= largest:
                res[i] = True

        return res
    

sol = Solution()
candy = [2,3,5,1,3]
extra = 3

print(sol.kidsWithCandies(candy, extra))