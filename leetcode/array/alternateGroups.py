from typing import List
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        circularColors = colors + colors[:k-1]
        left = 0
        count = 0
        for right in range(1, len(circularColors)):
            if circularColors[right] == circularColors[right-1]:
                left = right

            if right - left + 1 >= k:
                count += 1
        return count







    
sol = Solution()
print(sol.numberOfAlternatingGroups([0,1,0,1,0], 3))
print(sol.numberOfAlternatingGroups([0,1,0,0,1,0,1], 6))