def solution(X, A):
    # Implement your solution here
    stepMap = {i: 0 for i in range(1, X+1)}
    for i in range(len(A)):
        if A[i] in stepMap:
            stepMap.pop(A[i])
        if len(stepMap) == 0:
            return i
    return -1