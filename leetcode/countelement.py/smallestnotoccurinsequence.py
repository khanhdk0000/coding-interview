
# Find the smallest positive integer that does not occur in a given sequence.

def solution(A):
    # Implement your solution here
    numMap = {}
    maxVal = 0
    for i in A:
        if i not in numMap:
            numMap[i] = 0
        numMap[i] += 1
        maxVal = max(maxVal, i)

    for i in range(1, maxVal + 1):
        if i not in numMap:
            return i
    return maxVal + 1