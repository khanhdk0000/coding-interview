def solution(A):
    # Implement your solution here
    totalSum = sum(A)
    totalSum -= A[0]
    leftSum = A[0]
    res = abs(totalSum - leftSum)
    for i in range(1, len(A)- 1):
        leftSum += A[i]
        totalSum -= A[i]
        res = min(res, abs(totalSum - leftSum))

    return res