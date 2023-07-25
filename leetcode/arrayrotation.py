from typing import List
def solution(A: List, K):
    # Implement your solution here
    for i in range(K):
        lastVal = A.pop()
        A.insert(0, lastVal)
    return A


input = [3, 8, 9, 7, 6]
K = 3
print(solution(input, K))