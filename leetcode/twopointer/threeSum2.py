class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        LeetCode 15 - 3Sum

        Approach: Sort + Two Pointers
        - Sort the array, then for each element at index i, reduce the problem
          to a two-pointer twoSum on the subarray to the right.
        - Skip duplicate values of i to avoid duplicate triplets.
        - Inside twoSum, skip duplicate values of left after each match.

        Time Complexity : O(n^2)  — O(n log n) sort + O(n) outer loop × O(n) twoSum
        Space Complexity: O(n)    — O(n) for the sorted copy; output list excluded
        """
        res = []
        sorted_nums = sorted(nums)
        for i, val in enumerate(sorted_nums):
            if i > 0 and sorted_nums[i - 1] == val:
                continue
            two_sum_pairs = self.twoSum(sorted_nums, i + 1, -val)
            if len(two_sum_pairs) > 0:
                for pair in two_sum_pairs:
                    res.append([val, pair[0], pair[1]])
        return res

    def twoSum(self, nums: list[int], start: int, target: int) -> list[list[int]]:
        """
        Two-pointer scan on nums[start:] for pairs that sum to target.

        Time Complexity : O(n)  — each pointer moves at most n steps
        Space Complexity: O(1)  — excluding the output list
        """
        res = []
        left, right = start, len(nums) - 1
        while left < right:
            total = nums[left] + nums[right]
            if total == target:
                res.append([nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
            elif total < target:
                left += 1
            else:
                right -= 1
        return res
