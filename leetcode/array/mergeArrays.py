from typing import List
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        n1 = len(nums1)
        n2 = len(nums2)
        res = []
        i = 0
        j = 0
        while i < n1 and j < n2:
            if nums1[i][0] < nums2[j][0]:
                res.append(nums1[i])
                i += 1
            elif nums1[i][0] > nums2[j][0]:
                res.append(nums2[j])
                j += 1
            else:
                res.append([nums1[i][0], nums1[i][1] + nums2[j][1]])
                i += 1
                j += 1
        while i < n1:
            res.append(nums1[i])
            i += 1
        while j < n2:
            res.append(nums2[j])
            j += 1
        return res
# Time complexity: O(n1 + n2)
# Space complexity: O(n1 + n2)