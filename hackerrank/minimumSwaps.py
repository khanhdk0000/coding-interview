from typing import List


def minimumSwaps(arr: List[int]) -> int:
    # Value v belongs at index v-1. Each swap sends arr[i] straight home,
    # so every swap fixes at least one element.
    arr = arr[:]  # don't mutate caller's list
    swaps = 0
    for i in range(len(arr)):
        while arr[i] != i + 1:
            home = arr[i] - 1
            arr[i], arr[home] = arr[home], arr[i]
            swaps += 1
    return swaps


if __name__ == '__main__':
    assert minimumSwaps([7, 1, 3, 2, 4, 5, 6]) == 5
    assert minimumSwaps([4, 3, 1, 2]) == 3
    assert minimumSwaps([2, 3, 4, 1, 5]) == 3
    assert minimumSwaps([1, 3, 5, 2, 4, 6, 7]) == 3
    assert minimumSwaps([1]) == 0
    assert minimumSwaps([2, 1, 4, 3]) == 2  # two 2-cycles
    print("ok")
