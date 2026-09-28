from typing import List


def getMaxArrayCorrelation(a: List[int], b: List[int]) -> int:
    a = sorted(a)
    b = sorted(b)

    # max number of b values that can each beat a distinct a
    i = 0
    k = 0
    for v in b:
        if v > a[i]:
            k += 1
            i += 1

    # if any k values of b can be matched, the k largest can too
    total = 0
    for j in range(len(b) - k, len(b)):
        total += b[j]

    return total


if __name__ == "__main__":
    assert getMaxArrayCorrelation([1, 4, 2, 1, 3], [2, 3, 1, 2, 2]) == 7
    assert getMaxArrayCorrelation([1, 9, 4, 2], [8, 4, 3, 1]) == 15
    assert getMaxArrayCorrelation([1, 2, 3, 4, 5], [3, 5, 4, 6, 2]) == 20
    assert getMaxArrayCorrelation([5], [1]) == 0
    print("ok")
