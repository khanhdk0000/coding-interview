###
# Have the function PowerSetCount(arr) take the array of integers stored in arr, and return the length of the power set (the number of all possible sets) that can be generated. For example: if arr is [1, 2, 3], then the following sets form the power set: 

# [] 
# [1]
# [2]
# [3]
# [1, 2]
# [1, 3]
# [2, 3]
# [1, 2, 3] 

# You can see above all possible sets, along with the empty set, are generated. Therefore, for this input, your program should return 8.
###

def PowerSetCount(arr):
    # The length of the power set is 2^n, where n is the number of elements in the input set
    n = len(arr)
    return 2 ** n
