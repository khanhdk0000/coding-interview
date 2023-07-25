# "1. Coding question:
# Input: Sorted array [-6, -4, 0, 1, 2, 5]
# Output: An array sorted by square of each element in input array
# [0, 1, 4, 16, 25, 36]"


input = [-6, -4, 0, 1, 2, 5]
def process(arr):
    newArr = []
    negative = []
    for i in arr:
        if i < 0:
            negative.append(i)
        elif i >= 0:
            if len(negative) > 0:
                while len(negative) > 0 and abs(negative[-1]) < i:
                    newArr.append(abs(negative[-1])*abs(negative[-1]))
                    negative.pop()
            newArr.append(i*i)
    while len(negative) > 0:
        negaLast = negative.pop()
        newArr.append(negaLast*negaLast)
    print(newArr)
process(input)