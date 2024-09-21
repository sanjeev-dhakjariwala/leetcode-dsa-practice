# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


import heapq
from typing import *


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        # Sort the intervals by start time
        intervals.sort(key=lambda x: x.start)

        # Initialize a min-heap to keep track of end times
        heap = []

        # Add the end time of the first meeting
        heapq.heappush(heap, intervals[0].end)

        # Iterate over the remaining intervals
        for i in range(1, len(intervals)):
            # If the room is free (i.e., the meeting with the earliest end time ends before the current meeting starts)
            if heap[0] <= intervals[i].start:
                heapq.heappop(heap)

            # Add the end time of the current meeting
            heapq.heappush(heap, intervals[i].end)

        # The size of the heap is the minimum number of conference rooms required
        return len(heap)


sol = Solution()
intervals = [(0, 40), (5, 10), (15, 20)]
interval_objects = [Interval(start, end) for start, end in intervals]
print(sol.minMeetingRooms(interval_objects))
