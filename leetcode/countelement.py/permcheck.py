def solution(A):
    # Implement your solution here
    N = len(A)
    numMap = {i: 0 for i in range(1, N + 1)}
    for i in A:
        if i > N + 1:
            return 0
        if i in numMap:
            numMap.pop(i)
    if len(numMap) == 0:
        return 1
    return 0