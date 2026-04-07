from typing import List


# LeetCode 3731 — Find Missing Elements from Arrays
#
# Goal: return all integers in [min(nums), max(nums)] that are absent from nums,
#       in ascending order.
#
# ─────────────────────────────────────────────────────────────────────────────
# Approach 1: Your original (cleaned up)
# Issues in original:
#   • sorted() costs O(n log n) but was only used to find min/max → use min/max()
#   • numMap counted occurrences, but membership check is enough → use set()
#
# Time  : O(n + r)  where r = high - low (range size) — O(n) build set, O(r) scan
# Space : O(n)      — the set stores all n elements
# ─────────────────────────────────────────────────────────────────────────────
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        low, high = min(nums), max(nums)  # O(n), no need to sort
        seen = set(nums)  # O(n) — set lookup is O(1) vs dict
        # range(low, high+1) to be explicit; high is always in nums so never added
        return [i for i in range(low, high + 1) if i not in seen]

    # ─────────────────────────────────────────────────────────────────────────
    # Approach 2: Sort + two-pointer (O(1) extra space if sort is in-place)
    # Walk through the sorted array and collect gaps between consecutive elements.
    #
    # Time  : O(n log n)  — dominated by sort
    # Space : O(1)        — no extra data structures (output list not counted)
    # ─────────────────────────────────────────────────────────────────────────
    def findMissingElements_twopointer(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        for i in range(len(nums) - 1):
            # fill every integer strictly between nums[i] and nums[i+1]
            for missing in range(nums[i] + 1, nums[i + 1]):
                res.append(missing)
        return res
