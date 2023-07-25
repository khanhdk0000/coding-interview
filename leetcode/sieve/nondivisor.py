def sieve(n):
    F = [0] * (n + 1)
    i = 2
    while i * i <= n:
        if F[i] == 0:
            k = i * i
            while k <= n:
                if F[k] == 0:
                    F[k] = i
                k += i
        i += 1
    return F 

def factorials(x, F):
    primeFactors = {1}
    primeFactors.add(x)
    while F[x] > 0:
        primeFactors.add(x)
        primeFactors.add(F[x])
        x = x // F[x]
    primeFactors.add(x)
    return primeFactors

def solution(A):
    # Implement your solution here
    # print(A)
    if len(A) == 1:
        return [0]
    numMap = {}
    maxNum = A[0]
    for i in A:
        if i not in numMap:
            numMap[i] = 0
        numMap[i] += 1
        maxNum = max(maxNum, i)
    
    # sieve
    F = sieve(maxNum)
    res = []
    # print(numMap, F)
    for i in A:
        totalCount = 0
        sieveCur = factorials(i, F)
        # print(i, sieveCur)
        for j in sieveCur:
            if j in numMap:                    
                count = numMap[j]
                if j == i:
                    count -= 1
                totalCount += count
        res.append(len(A)- 1 - totalCount)
    return res

def solution2(A):
    div = {}
    for elem in A:
        div[elem] = set([1, elem])
    print(div)

    A_max = max(A)
    idx = 2
    while idx * idx <= A_max:
        elem = idx
        while elem <= A_max:
            if elem in div and not idx in div[elem]:
                div[elem].add(idx)
                div[elem].add(elem // idx)
            elem += idx
        idx += 1
    print(div)

    count = {}
    for elem in A:
        if elem not in count:
            count[elem] = 1
        else:
            count[elem] += 1
    print(count)

    result = [0]*len(A)
    for idx, elem in enumerate(A):
        tmp = 0
        for value in div[elem]:
            tmp += count.get(value, 0)
        
        result[idx] = len(A) - tmp

    return result

input = [1,1]
# print(solution([1,1]))
# print(solution([2,4]))
# print(solution([3,1,2,3,6]))
# print(solution([6, 7, 2, 1, 4, 7, 4, 4, 1, 8, 10, 15]))
print(solution2([6, 7, 2, 1, 4, 7, 4, 4, 1, 8, 10, 15]))
