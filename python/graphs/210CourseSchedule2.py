from typing import *
from collections import *

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Build the adjacency list representation of the graph
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1

        # Perform BFS (Kahn's algorithm) to find topological ordering
        result = []
        queue = deque()

        # Enqueue courses with in-degree zero (no prerequisites)
        for course in range(numCourses):
            if in_degree[course] == 0:
                queue.append(course)

        while queue:
            course = queue.popleft()
            result.append(course)

            # Decrement in-degree of adjacent courses
            for adj_course in graph[course]:
                in_degree[adj_course] -= 1
                if in_degree[adj_course] == 0:
                    queue.append(adj_course)

        # Check if all courses are taken
        if len(result) != numCourses:
            return []
        return result
