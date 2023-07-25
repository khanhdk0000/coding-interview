def solution(A):
    # Implement your solution here
    numMap = {i: 0 for i in range(1, len(A) + 1)}
    for i in A:
        if i in numMap:
            numMap.pop(i)

    for j in numMap.keys():
        return j
    return 0