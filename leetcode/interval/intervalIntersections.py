class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        intersections = []
        i,j = 0,0
        while i < len(firstList) and j < len(secondList):
            if firstList[i][0] <= secondList[j][0]:
                start, end = firstList[i], secondList[j]
            else:
                start, end = secondList[j], firstList[i]

            if start[1] >= end[0]:
                intersections.append([end[0], min(start[1], end[1])])
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
        return intersections