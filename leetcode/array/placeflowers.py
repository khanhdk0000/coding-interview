from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1:
            if (flowerbed[0] == 0 and n == 1) or n == 0:
                return True
            else:
                return False
        
        for i in range(len(flowerbed)):
            if n == 0:
                return True
            print(flowerbed, n)
            if i == 0:
                if flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                    n -= 1
                    flowerbed[i] = 1
            elif i == len(flowerbed) - 1:
                if flowerbed[i - 1] == 0 and flowerbed[i] == 0:
                    n -= 1
                    flowerbed[i] = 1
            else:
                if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                    n -= 1
                    flowerbed[i] = 1

        print(n)
        return n == 0


sol = Solution()
flower = [0,0,1,0,0]
n = 1

print(sol.canPlaceFlowers(flower, n))