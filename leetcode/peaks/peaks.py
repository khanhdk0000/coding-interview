def solution(A):
    # Implement your solution here
    peaks = []
    for i in range(1, len(A)-1):
        if A[i-1] < A[i] and A[i] > A[i+1]:
            peaks.append(i)
    N = len(A)
    maxPossible = len(peaks)
    for i in range(maxPossible, 0, -1):
        if N % i == 0:
            blockLen = N // i
            blocks = [0]*i
            for p in peaks:
                pos = p // blockLen
                if blocks[pos] == 0:
                    blocks[pos] = 1
            if blocks.count(1) == i:
                return i
    return 0

input = [1,2,3,4,3,4,1,2,3,4,6,2]
print(solution(input))