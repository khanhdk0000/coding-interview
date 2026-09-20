from typing import List


def countSubarraysWithSumAndMaxAtMost(nums: List[int], k: int, M: int) -> int:
    """Count subarrays with sum == k and every element <= M.

    Elements > M are barriers: no valid subarray crosses one. Inside each
    barrier-free segment this is LeetCode 560 (prefix sum + counter).
    """
    count = 0
    seen = {0: 1}
    total = 0
    for x in nums:
        if x > M:
            seen = {0: 1}  # reset segment
            total = 0
            continue
        total += x
        count += seen.get(total - k, 0)
        seen[total] = seen.get(total, 0) + 1
    return count


if __name__ == "__main__":
    assert countSubarraysWithSumAndMaxAtMost([2, -1, 2, 1, -2, 3], 3, 2) == 2
    assert countSubarraysWithSumAndMaxAtMost([], 0, 0) == 0
    assert countSubarraysWithSumAndMaxAtMost([5], 5, 5) == 1
    assert countSubarraysWithSumAndMaxAtMost([5], 5, 4) == 0  # element above M
    assert countSubarraysWithSumAndMaxAtMost([1, 2, 3], 3, 10) == 2  # [1,2] and [3]
    assert countSubarraysWithSumAndMaxAtMost([1, 2, 3], 3, 2) == 1  # 3 barred, only [1,2]
    assert countSubarraysWithSumAndMaxAtMost([0, 0, 0], 0, 1) == 6  # every subarray
    assert countSubarraysWithSumAndMaxAtMost([1, 9, 2], 3, 5) == 0  # 9 splits, no crossing
    print("ok")
