from typing import List
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Step 1: Build the graph and indegree array
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        # Step 2: Initialize the queue with courses that have no prerequisites
        queue = []
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        # Step 3: Perform BFS
        order = []
        while queue:
            course = queue.pop(0)
            order.append(course)

            for neighbor in graph[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # Step 4: Check if we were able to take all courses
        if len(order) == numCourses:
            return order
        else:
            return []