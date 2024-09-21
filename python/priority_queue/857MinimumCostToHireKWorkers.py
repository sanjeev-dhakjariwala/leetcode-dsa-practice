import heapq
from typing import *
from collections import *

class Solution:
    def mincostToHireWorkers(
        self, quality: List[int], wage: List[int], k: int
    ) -> float:
        # Calculate the wage-to-quality ratios
        ratios = [(w / q, q) for w, q in zip(wage, quality)]
        ratios.sort()  # Sort workers by their wage-to-quality ratio
        print(ratios)
        min_cost = float("inf")
        quality_sum = 0
        heap = []

        for ratio, q in ratios:
            # Add quality to heap
            heapq.heappush(heap, -q)
            quality_sum += q

            if len(heap) > k:
                # Remove the worker with the highest quality from the heap
                quality_sum += heapq.heappop(heap)

            if len(heap) == k:
                # Calculate the total wage for the current group
                min_cost = min(min_cost, ratio * quality_sum)

        return min_cost

sol = Solution()
quality = [10, 20, 5]
wage = [70, 50, 30]
print(sol.mincostToHireWorkers(quality, wage, 2))