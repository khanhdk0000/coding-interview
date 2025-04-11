class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def isSymmetric(n: int) -> bool:
            s = str(n)
            l = len(s)
            if l % 2 != 0:
                return False
            mid = l // 2
            left = s[:mid]
            right = s[mid:]
            return sum(int(c) for c in left) == sum(int(c) for c in right)
        
        count = 0
        for i in range(low, high + 1):
            if isSymmetric(i):
                count += 1
        return count
    
# Time Complexity: O(n * m), where n is the range of numbers and m is the number of digits in the largest number.