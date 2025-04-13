# For this challenge you will be determining the next largest palindrome.
# have the function NextPalindrome(num) take the num parameter being passed and return the next largest palindromic number. The input can be any positive integer. For example: if num is 24, then your program should return 33 because that is the next largest number that is a palindrome.

def NextPalindrome(num):
    # ## 99, 999, 9999, 99999, 999999, 9999999
    # # Edge case for all 9's
    # if num == int('9' * len(str(num))):
    #     return num + 2
    
    # # Edge case for 10, 100, 1000, 10000, 100000
    # if num == 10 ** (len(str(num)) - 1):
    #     return num + 1

    def buildPalindrome(base, isEven):
        if isEven:
            return int(base + base[::-1])
        else:
            return int(base + base[-2::-1])

    strNum = str(num)
    isEven = len(strNum) % 2 == 0
    midIdx = len(strNum) // 2 if isEven else len(strNum) // 2 + 1
    base = strNum[:midIdx]
    nextPalindrome = buildPalindrome(str(int(base)), isEven)
    if nextPalindrome > num:
        return nextPalindrome

    return buildPalindrome(str(int(base) + 1), isEven)

print(NextPalindrome(24))  # Output: 33
print(NextPalindrome(123))  # Output: 131
print(NextPalindrome(999))  # Output: 1001
print(NextPalindrome(9999))  # Output: 10001
print(NextPalindrome(1001))  # Output: 1111
print(NextPalindrome(1111))  # Output: 1221
print(NextPalindrome(899))  # Output: 909