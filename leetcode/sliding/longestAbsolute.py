from typing import List
from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_d = deque()           # decreasing → front is max
        min_d = deque()           # increasing → front is min
        left   = 0
        best   = 0

        for right, val in enumerate(nums):
            # maintain max deque (decreasing)
            while max_d and val > max_d[-1]:
                max_d.pop()
            max_d.append(val)

            # maintain min deque (increasing)
            while min_d and val < min_d[-1]:
                min_d.pop()
            min_d.append(val)

            # shrink window until it's valid
            while max_d[0] - min_d[0] > limit:
                if nums[left] == max_d[0]:
                    max_d.popleft()
                if nums[left] == min_d[0]:
                    min_d.popleft()
                left += 1

            best = max(best, right - left + 1)

        return best