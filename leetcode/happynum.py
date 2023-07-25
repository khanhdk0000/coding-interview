class Solution:
    def getSquare(self, n):
        square, tmp = 0, 0
        while n > 0:
            tmp = n % 10
            square += tmp * tmp
            n /= 10
        return square

    def isHappy(self, n: int) -> bool:
        resMap = {}
        tmp = self.getSquare(n)
        if tmp == 1:
            return True
        while True:
            if tmp in resMap:
                return False
            elif tmp == 1:
                return True
            else:
                resMap[tmp] = 1
            tmp = self.getSquare(n)


sol = Solution()
sol.isHappy(100)
