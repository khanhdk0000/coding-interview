class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]
        for val in intervals[1:]:
            start = merged[-1]
            if start[1] < val[0]:
                merged.append(val)
            else:
                merged[-1] = [start[0], max(start[1], val[1])]
        return merged