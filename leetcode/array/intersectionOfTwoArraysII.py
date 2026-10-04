from collections import Counter
from typing import List


class Solution:
    # 350. Intersection of Two Arrays II — keep duplicates (min count in both)
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list((Counter(nums1) & Counter(nums2)).elements())

    # One hash map of counts, scan the other array
    # Time O(n + m), Space O(n) — only nums1 is stored
    # Pass the smaller array as nums1 for O(min(n, m)) space
    def intersect_hashmap(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Initialize seen dictionary and res array
        seen = {}
        result = []

        # count values occurring in nums1
        for x in nums1:
            seen[x] = seen.get(x, 0) + 1

        for x in nums2:
            # Check if x still has unmatched copies from nums1
            if seen.get(x, 0) > 0:
                result.append(x)
                seen[x] -= 1

        # Return the result
        return result


if __name__ == "__main__":
    s = Solution()
    for f in (s.intersect, s.intersect_hashmap):
        assert sorted(f([1, 2, 2, 1], [2, 2])) == [2, 2]
        assert sorted(f([4, 9, 5], [9, 4, 9, 8, 4])) == [4, 9]
        assert sorted(f([1, 2, 2, 1], [2])) == [2]
        assert f([], [1]) == []
    print("ok")
