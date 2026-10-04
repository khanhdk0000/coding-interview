from typing import List


class Solution:
    # 349. Intersection of Two Arrays — unique common elements

    # Approach 1: two sets
    # Time O(n + m), Space O(n + m)
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set2 & set1)

    # Approach 2: sort + two pointers
    # Time O(n log n + m log m), Space O(1) extra besides sort + output
    # Note: sorts inputs in place
    def intersection_two_pointers(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Sort both arrays
        nums1.sort()
        nums2.sort()

        # Initialize two pointers
        N = len(nums1)
        M = len(nums2)
        p1 = 0
        p2 = 0

        # Create set that stores integers appearing in both arrays
        intersection = set()

        while p1 < N and p2 < M:
            # Add a value to the set if values at both pointers equal
            if nums1[p1] == nums2[p2]:
                intersection.add(nums1[p1])
                p1 += 1
                p2 += 1
            elif nums1[p1] < nums2[p2]:
                p1 += 1
            else:
                p2 += 1

        # Convert intersection to an array
        return list(intersection)

    # Approach 3: two sets, manually iterate the smaller one
    # Time O(n + m), Space O(n + m)
    # Same as approach 1 — built-in `&` already iterates the smaller set
    def set_intersection(self, set1: set, set2: set) -> List[int]:
        return [x for x in set1 if x in set2]

    def intersection_smaller_set(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)

        if len(set1) < len(set2):
            return self.set_intersection(set1, set2)
        else:
            return self.set_intersection(set2, set1)

    # Approach 4: one hash map, scan the other array
    # Time O(n + m), Space O(n) — only nums1 is stored
    # Pass the smaller array as nums1 for O(min(n, m)) space
    def intersection_hashmap(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Initialize seen dictionary and res array
        seen = {}
        result = []

        # mark values occurring in nums1
        for x in nums1:
            seen[x] = 1

        for x in nums2:
            # Check if x is in the dictionary and not in the result
            if x in seen and seen[x] == 1:
                result.append(x)
                seen[x] = 0

        # Return the result
        return result


if __name__ == "__main__":
    s = Solution()
    for f in (s.intersection, s.intersection_two_pointers, s.intersection_smaller_set, s.intersection_hashmap):
        assert sorted(f([1, 2, 2, 1], [2, 2])) == [2]
        assert sorted(f([4, 9, 5], [9, 4, 9, 8, 4])) == [4, 9]
        assert f([], [1]) == []
    print("ok")
