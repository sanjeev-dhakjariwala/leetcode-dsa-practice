from typing import *
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(point):
            return point[0] ** 2 + point[1] ** 2

        # Use a min heap to store points based on their distances
        heap = [(distance(point), point) for point in points]
        heapq.heapify(heap)
        print(heap)
        # Extract k closest points from the heap
        result = [heapq.heappop(heap)[1] for _ in range(k)]
        return result


sol = Solution()
print(sol.kClosest([[1, 3], [-2, 2]], 1))
