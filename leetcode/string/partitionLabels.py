from typing import List
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Create a dictionary to store the last position of each character, 
        lastPosition = { c: i for i, c in enumerate(s)}
        partitions = []
        start, end = 0, 0
        
        # Iterate through the string, updating the end position for each character
        for i, c in enumerate(s):
            end = max(end, lastPosition[c])
            if i == end:
                partitions.append(end - start + 1)
                start = end + 1
        return partitions