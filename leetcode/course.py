from typing import List,  Optional
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courseMap = {}
        for course in prerequisites:
            a, b = course
            if b not in courseMap:
                courseMap[b] = [a]
            else:
                courseMap[b].append(a)
        # find start course
        courses = {}
        for _, value in courseMap.items():
            courses.add(value)
        firstCourse = -1
        for key, _ in courseMap.items():
            if key not in courses:
                firstCourse = key
                break
        
        res = {}
        res.add(firstCourse)
        for c in courseMap[firstCourse]:
            if len(res) == numCourses:
                return list(res)
            res.add(c)
        # for c in courseMap[firstCourse]:
        #     if c in courseMap.keys():
        #         for x in courseMap[c]:

    def findCourse()

    
# [[1,0],[2,0],[3,1],[3,2]]
'''
0: 1, 2
1: 3
2: 3
'''