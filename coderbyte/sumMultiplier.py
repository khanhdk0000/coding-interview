# /
#               CODERBYTE SUM MULTIPLIER CHALLENGE               
                                                               
#   Problem Statement                                            
#   Have the function SumMultiplier(arr) take the array of       
#   numbers stored in arr and return the string true if any two  
#   numbers can be multiplied so that the answer is greater than 
#   double the sum of all the elements in the array. If not,     
#   return the string false.                                     
#   For example: if arr is [2, 5, 6, -6, 16, 2, 3, 6, 5, 3] then 
#   the sum of all these elements is 42 and doubling it is 84.   
#   There are two elements in the array, 16  6 = 96 and 96 is   
#   greater than 84 so your program should return the string true
                                                               
#   Examples                                                     
#   Input 1: [2, 2, 2, 2, 4, 1]                                  
#   Output 1: false                                              
                                                               
#   Input 2: [1, 1, 2, 10, 3, 1, 12]                             
#   Output 2: true                                               
                                                               
#  /

def SumMultiplier(arr):
    total = sum(arr)
    target = 2 * total

    # Sort descending to get largest + most negative easily
    arr.sort()

    # Check top 2 positive numbers
    max1 = arr[-1]
    max2 = arr[-2] if len(arr) >= 2 else float('-inf')

    # Check bottom 2 negative numbers
    min1 = arr[0]
    min2 = arr[1] if len(arr) >= 2 else float('-inf')

    candidates = [
        max1 * max2,
        min1 * min2
    ]

    if any(prod > target for prod in candidates):
        return "true"
    return "false"

print(SumMultiplier([2, 5, 6, -6, 16, 2, 3, 6, 5, 3]))  # Output: true
print(SumMultiplier([2, 2, 2, 2, 4, 1]))  # Output: false
print(SumMultiplier([1, 1, 2, 10, 3, 1, 12]))  # Output: true