class Solution:
    def isHappy(self, n: int) -> bool:
        slow = fast = n
        while True:
            slow = self.get_next_num(slow)
            fast = self.get_next_num(self.get_next_num(fast))

            if fast == 1:
                return True
            if slow == fast:
                return False
    
    def get_next_num(self, num) -> int:
        next_num = 0
        while num > 0:
            digit = num % 10
            num = num // 10
            next_num += digit ** 2
        return next_num