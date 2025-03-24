from typing import List
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])

        # Merge intervals
        merged = []
        currentStart, currentEnd = meetings[0]

        for i in range(1, len(meetings)):
            start, end = meetings[i]
            if start <= currentEnd:
                currentEnd = max(currentEnd, end)
            else:
                merged.append([currentStart, currentEnd])
                currentStart = start
                currentEnd = end
        
        merged.append([currentStart, currentEnd])
        coveredDays = 0
        for start, end in merged:
            coveredDays += end - start + 1
        
        return days - coveredDays