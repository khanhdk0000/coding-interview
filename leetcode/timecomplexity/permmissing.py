def solution(A):
    # Implement your solution here
    N = len(A)
    totalSum = (N + 1)*(N + 2) // 2
    realSum = sum(A)
    return totalSum - realSum