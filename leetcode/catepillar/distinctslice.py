def solution(M, A):
    # Implement your solution here
    N = len(A)
    res = 0
    for i in range(N):
        numMap = {}
        start = i
        end = i
        while end < N:
            if A[end] in numMap:
                break
            numMap[A[end]] = 0
            # print(start, end)
            res += 1
            end += 1
    return res

def count_distinct_slices(A):
    N = len(A)
    numMap = {}
    start = 0
    end = 0
    count = 0
    
    while end < N:
        if A[end] in numMap and numMap[A[end]] >= start:
            start = numMap[A[end]] + 1
        numMap[A[end]] = end
        count += end - start + 1
        end += 1
    
    return count

input = [3,4,5,5,2]
# print(solution(6, input))
print(count_distinct_slices(input))

