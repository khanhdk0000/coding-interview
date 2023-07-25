from typing import List
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        i = 0
        while i < len(citations) and citations[i] >= (i+1):
            i += 1
        return i


input = [3,0,6,1,5]
sol = Solution()

print(sol.hIndex(input))