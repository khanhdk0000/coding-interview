def solution(A):
    # Implement your solution here
    numMap = {}
    for i in A:
        if abs(i) not in numMap:
            numMap[abs(i)] = 0

    return len(numMap)

input = [-5, -3, -1, 0, 3, 2147483647]
print(solution(input))