from typing import List,  Optional

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        X = len(nums)
        low = 0
        high = X-1
        mid = 0
        pivot = False
        while high >= low:
            mid = (high + low) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                if mid < high and nums[mid] > nums[mid+1]:
                    break
                if mid > 0 and nums[mid] < nums[mid-1] and nums[0] <= target:
                    low = 0
                    high = mid - 1
                    pivot = True
                else:
                    low = mid + 1
            else:
                if mid < high and nums[mid] > nums[mid+1] and nums[X - 1] >= target:
                    low = mid + 1
                    high = X - 1
                    pivot = True
                else:
                    high = mid - 1
                    if nums[0] > target and not pivot:
                        low = mid + 1
                        high = X - 1

        return -1
    
# [3,4,5,6,1,2]
sol = Solution()
input = [3,4,5,6,1,2]


print(sol.search(input, 2))