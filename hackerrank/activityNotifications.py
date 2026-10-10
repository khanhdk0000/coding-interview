from typing import List


def activityNotifications(expenditure: List[int], d: int) -> int:
    # Values are 0..200, so keep the window as a count array (counting sort).
    count = [0] * 201
    for v in expenditure[:d]:
        count[v] += 1

    def kth(k):  # k-th smallest (0-indexed) value in the window
        seen = 0
        for v in range(201):
            seen += count[v]
            if seen > k:
                return v

    notices = 0
    for i in range(d, len(expenditure)):
        # 2 * median, kept as an int to avoid float division
        if d % 2:
            double_median = 2 * kth(d // 2)
        else:
            double_median = kth(d // 2 - 1) + kth(d // 2)
        if expenditure[i] >= double_median:
            notices += 1
        count[expenditure[i - d]] -= 1  # slide window: drop oldest day
        count[expenditure[i]] += 1      # add today
    return notices


if __name__ == '__main__':
    assert activityNotifications([10, 20, 30, 40, 50], 3) == 1
    assert activityNotifications([2, 3, 4, 2, 3, 6, 8, 4, 5], 5) == 2
    assert activityNotifications([1, 2, 3, 4, 4], 4) == 0
    assert activityNotifications([1, 3, 5, 7], 2) == 1  # even d: day 3 window [1,3] -> 5 >= 4 notice; day 4 window [3,5] -> 7 < 8 none
    print("ok")
