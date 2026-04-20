from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        LeetCode 496 - Next Greater Element I

        Approach: Monotonic Stack + HashMap
        - Traverse nums2 with a decreasing monotonic stack.
        - Whenever a larger element is found, it is the "next greater" for all
          elements currently in the stack that are smaller than it.
        - Store the mapping {element -> next_greater_element} in a hashmap.
        - Answer each query in nums1 with an O(1) hashmap lookup.

        Time Complexity : O(n + m)  — n = len(nums2), m = len(nums1)
        Space Complexity: O(n)      — hashmap + stack, both bounded by nums2
        """
        next_greater = {}
        stack = []
        for val in nums2:
            while stack and stack[-1] < val:
                next_greater[stack.pop()] = val
            stack.append(val)
        
        result = [-1] * len(nums1)
        for i, val in enumerate(nums1):
            result[i] = next_greater.get(val, -1)
        return result
