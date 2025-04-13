#  For this challenge you will determine the largest double digit number.
# have the function LargestPair(num) take the num parameter being passed and determine the largest double digit number within the whole number. For example: if num is 4759472 then your program should return 94 because that is the largest double digit number. The input will always contain at least two positive digits. 

def LargestPair(num):
    result = 0
    num = str(num)
    for i in range(len(num) - 1):
        pair = int(num[i:i + 2])
        if pair > result:
            result = pair
    return result

print(LargestPair(4759472))  # Output: 94
print(LargestPair(123456))  # Output: 56
print(LargestPair(99))  # Output: 99
print(LargestPair(1001))  # Output: 10
print(LargestPair(9876543210))  # Output: 98
