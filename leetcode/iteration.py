from typing import List
def solution(N) -> int:
    binary_digits = []

    while N > 0:
        binary_digits.append(N % 2)
        N //= 2

    binDigits = ''.join(str(digit) for digit in binary_digits[::-1])
    print(binDigits)

    i, j, res = 0, 0, 0
    for j in range(1, len(binDigits)):
        if binDigits[j] == '1':
            # print(i, j)
            res = max(res, j - i -1)
            i = j

    return res

input = 1041
print(solution(input))
# 10000010001