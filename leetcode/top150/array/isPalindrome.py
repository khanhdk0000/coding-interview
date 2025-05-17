class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join([i for i in s if i.isalnum()])
        return s == s[::-1]

    def isPalindrome2(self, s: str) -> bool:
        # sliding window, 2 pointers
        s = s.lower()
        s = ''.join([i for i in s if i.isalnum()])
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True