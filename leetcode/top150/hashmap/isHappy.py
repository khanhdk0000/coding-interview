class Solution:
    def isHappy(self, n: int) -> bool:
        def getNext(n):
            totalSum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                totalSum += digit ** 2
            return totalSum
        seen = {}
        while n != 1 and n not in seen:
            seen[n] = True
            n = getNext(n)
        return n == 1