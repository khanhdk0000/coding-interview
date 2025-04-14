# Challenge
# The function ProductDigits(num) take the num parameter being passed which will be a positive integer, and determine the least amount of digits you need to multiply to produce it. For example: if num is 24 then you can multiply 8 by 3 which produces 24, so your program should return 2 because there is a total of only 2 digits that are needed. Another example: if num is 90, you can multiply 10 * 9, so in this case your program should output 3 because you cannot reach 90 without using a total of 3 digits in your multiplication. 
# Sample Test Cases
# Input:6
# Output:2

# Input:23
# Output:3
import math
def ProductDigits(num):

    
    min_len = 1 + len(str(num))

    # check every divisor up to √num (inclusive)
    for i in range(2, math.isqrt(num) + 1):
        if num % i == 0:
            j = num // i
            digits = len(str(i)) + len(str(j))
            min_len = min(min_len, digits)

    return min_len

print(ProductDigits(24))  # Expected output: 2 (8 * 3)
print(ProductDigits(90))  # Expected output: 3 (10 * 9)
print(ProductDigits(6))   # Expected output: 2 (2 * 3)
print(ProductDigits(23))  # Expected output: 3 (2 * 11)