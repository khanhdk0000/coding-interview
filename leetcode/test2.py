# def solution(A):
#     A.sort()
#     n = len(A)
#     ans = 0
#     for i in range(n):
#         for j in range(i+1, n):
#             diff = A[j] - A[i]
#             chosen = [A[i], A[j]]

#             for k in range(j+1, n):
#                 if A[k] - chosen[-1] == diff:
#                     chosen.append(A[k])
#             ans = max(ans, len(chosen))
#     return ans

def solution(A):
    n = len(A)
    A.sort()
    maxNum = max(A)
    numMap = {}
    for i in A:
        if i not in numMap:
            numMap[i] = 0
        numMap[i] += 1

    res = 0
    for i in range(n):
        for j in range(i + 1, n):
            diff = A[j] - A[i]
            curLen = 2
            nxtNum = A[j] + diff

            if diff == 0:
                curLen = numMap[A[i]]
            else:
                while nxtNum in numMap and nxtNum <= maxNum:
                    curLen += 1
                    nxtNum += diff
            if curLen > res:
                res = curLen
    return res

# input = [18,26,18,24,24,20,22]
# print(solution(input))
# input = [4,7,1,5,3]
# print(solution(input))
# input = [12,12,12,15,10]
# print(solution(input))
# input = [4,3,5,1,4,4]
# print(solution(input))
input = [4,3,5,1,4,4,7,9,10,100]
print(solution(input))
input = [10,4,8,8,8,7,1,8,8]
print(solution(input))
