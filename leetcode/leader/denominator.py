# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    if len(A) == 0:
        return -1
    value = A[0]
    size = 0
    for i in A:
        if size == 0:
            size += 1
            value = i
        else:
            if i != value:
                size -= 1
            else:
                size += 1

    candidate = -1
    if size > 0:
        candidate = value
    count = 0
    indexList = []
    for idx in range(len(A)):
        if A[idx] == candidate:
            count += 1
            indexList.append(idx)
            
    if count <= len(A) // 2:
        return -1
    return indexList[0]