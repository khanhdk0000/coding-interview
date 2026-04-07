from typing import List


# LeetCode 3034 — Number of Subarrays That Match a Pattern I
#
# Key insight: first convert nums into a "trend array" t of size n-1 where:
#   t[k] =  1 if nums[k+1] > nums[k]
#   t[k] =  0 if nums[k+1] == nums[k]
#   t[k] = -1 if nums[k+1] < nums[k]
# Then the problem becomes: count how many windows of length m in t equal pattern.
# This is exactly substring/subarray matching.
#
# ─────────────────────────────────────────────────────────────────────────────
# Approach 1: Sliding window brute force (your original, cleaned up)
# Time  : O(n * m)  — (n - m) windows × m comparisons each
# Space : O(1)      — no extra data structures
# Fine for this problem: n ≤ 100, so worst case 100*100 = 10,000 ops
# ─────────────────────────────────────────────────────────────────────────────
class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n, m = len(nums), len(pattern)
        res = 0
        for i in range(n - m):
            satisfied = True
            for k in range(m):
                a, b = nums[i + k], nums[i + k + 1]
                if pattern[k] == 1 and not (b > a):
                    satisfied = False
                    break
                if pattern[k] == 0 and not (b == a):
                    satisfied = False
                    break
                if pattern[k] == -1 and not (b < a):
                    satisfied = False
                    break
            if satisfied: 
                res += 1
        return res
    

    # ─────────────────────────────────────────────────────────────────────────
    # Approach 2: Convert to trend array + KMP
    # Time  : O(n + m)  — linear! (KMP failure function + single scan)
    # Space : O(n + m)  — trend array + KMP failure table
    #
    # Why KMP? After converting nums → trend array t, matching pattern inside t
    # is identical to substring search. KMP avoids re-scanning already-matched
    # characters, bringing it from O(n*m) down to O(n+m).
    # ─────────────────────────────────────────────────────────────────────────
    def countMatchingSubarrays_kmp(self, nums: List[int], pattern: List[int]) -> int:
        n, m = len(nums), len(pattern)

        def trend(a, b):
            return 1 if b > a else (-1 if b < a else 0)

        # Build trend array from nums (length n-1)
        t = [trend(nums[k], nums[k + 1]) for k in range(n - 1)]

        # Build KMP failure (LPS) table for pattern
        lps = [0] * m
        length, i = 0, 1
        while i < m:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            elif length:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

        # KMP search: find pattern in t
        res = 0
        j = 0  # pointer in pattern
        for i in range(len(t)):
            while j > 0 and t[i] != pattern[j]:
                j = lps[j - 1]
            if t[i] == pattern[j]:
                j += 1
            if j == m:
                res += 1
                j = lps[j - 1]
        return res
