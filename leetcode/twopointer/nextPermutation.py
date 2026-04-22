from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        LeetCode 31 - Next Permutation

        Approach: Staged Two-Pointer Traversal
        ----------------------------------------
        The next permutation is the lexicographically smallest arrangement that
        is strictly larger than the current one. The algorithm has four stages:

        1. LOCATE THE PIVOT
           Scan from right to left to find the first index `pivot` where the
           non-increasing suffix is broken, i.e. nums[pivot] < nums[pivot + 1].
           - The suffix to the right of the pivot is non-increasing (already at
             its largest permutation), so rearranging only within the suffix
             won't help — we must involve the pivot.
           - Example: [1, 2, 3, 5, 4, 4, 1]
                             ^pivot (value 3, since 3 < 5)

        2. HANDLE "ALREADY LARGEST" CASE
           If no pivot is found (pivot == -1), the entire array is non-increasing,
           meaning it is already the largest permutation. Reversing it gives the
           smallest permutation.
           - Example: [5, 4, 3, 2, 1] → reverse → [1, 2, 3, 4, 5]

        3. FIND THE RIGHTMOST SUCCESSOR
           To make the smallest possible increase at the pivot position, swap the
           pivot with the rightmost element in the suffix that is strictly greater
           than the pivot. Because the suffix is non-increasing, traversing it
           from right to left yields the closest (smallest) such value.
           - Example: pivot = 3 (index 2), suffix = [5, 4, 4, 1]
                      rightmost value > 3 from the right → 4 (rightmost one)

        4. SWAP + REVERSE SUFFIX
           - Swap pivot with the rightmost successor to bump up the pivot digit
             with the smallest possible increase.
           - After the swap the suffix is still non-increasing (swapping with the
             rightmost successor preserves this property).
           - Reverse the suffix to turn it into its smallest permutation (i.e.
             non-decreasing), which minimises the overall number.
           - Example after swap: [1, 2, 4, 5, 4, 3, 1]
                      after reverse suffix: [1, 2, 4, 1, 3, 4, 5]

        Time Complexity : O(n) — at most two linear scans + one reversal
        Space Complexity: O(1) — all operations are in-place
        """
        pivot = len(nums) - 2

        # Stage 1: Locate the pivot (first element that breaks non-increasing order from the right)
        while pivot >= 0 and nums[pivot] >= nums[pivot + 1]:
            pivot -= 1

        # Stage 2: No pivot → already the largest permutation; reverse to get the smallest
        if pivot == -1:
            nums.reverse()
            return

        # Stage 3: Find rightmost successor — rightmost element in suffix strictly greater than pivot
        right_successor = len(nums) - 1
        while nums[right_successor] <= nums[pivot]:
            right_successor -= 1

        # Stage 4a: Swap pivot with its rightmost successor to make the smallest increase
        nums[pivot], nums[right_successor] = nums[right_successor], nums[pivot]

        # Stage 4b: Reverse the suffix after pivot to minimise its permutation
        nums[pivot + 1 :] = reversed(nums[pivot + 1 :])
