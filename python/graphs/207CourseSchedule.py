from collections import defaultdict, deque
from typing import *


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1

        # Initialize a queue with courses having in-degree 0
        queue = deque()
        for course in range(numCourses):
            if in_degree[course] == 0:
                queue.append(course)

        # Perform topological sorting
        while queue:
            current_course = queue.popleft()
            for neighbor in graph[current_course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Check if all courses have in-degree 0
        return all(deg == 0 for deg in in_degree)


sol = Solution()
print(sol.canFinish(5, [[1, 0], [2, 1], [3, 2], [4, 3]]))
