from typing import List


def countResponseTimeRegressions(responseTimes: List[int]) -> int:
    """Count responseTimes[i], i >= 1, strictly greater than average of responseTimes[0..i-1]."""
    total = 0
    count = 0
    for i, x in enumerate(responseTimes):
        # ponytail: integer compare x > total/i, no float rounding
        if i and x * i > total:
            count += 1
        total += x
    return count


if __name__ == "__main__":
    assert countResponseTimeRegressions([100, 200, 150, 300]) == 2
    assert countResponseTimeRegressions([]) == 0
    assert countResponseTimeRegressions([100]) == 0
    assert countResponseTimeRegressions([5, 5, 5]) == 0
    assert countResponseTimeRegressions([1, 2, 3, 4]) == 3
    print("ok")
