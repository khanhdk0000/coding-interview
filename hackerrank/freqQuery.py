from collections import Counter
from typing import List


def freqQuery(queries: List[List[int]]) -> List[int]:
    count = Counter()  # value -> how many times it appears
    freq = Counter()   # frequency -> how many values have that frequency
    out = []
    for op, v in queries:
        if op == 1:
            freq[count[v]] -= 1
            count[v] += 1
            freq[count[v]] += 1
        elif op == 2:
            if count[v] > 0:
                freq[count[v]] -= 1
                count[v] -= 1
                freq[count[v]] += 1
        else:
            out.append(1 if freq[v] > 0 else 0)
    return out


if __name__ == '__main__':
    assert freqQuery([[1, 1], [2, 2], [3, 2], [1, 1], [1, 1], [2, 1], [3, 2]]) == [0, 1]
    assert freqQuery([[1, 5], [1, 6], [3, 2], [1, 10], [1, 10], [1, 6], [2, 5], [3, 2]]) == [0, 1]
    assert freqQuery([[3, 4], [2, 1003], [1, 16], [3, 1]]) == [0, 1]
    assert freqQuery([[2, 7], [3, 1]]) == [0]  # delete missing value must not corrupt freq
    print("ok")
