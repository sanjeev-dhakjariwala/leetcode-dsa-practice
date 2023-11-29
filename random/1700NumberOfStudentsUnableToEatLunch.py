import collections
from typing import *


class Solution:
    def countStudents(self, students, sandwiches):
        circular, square = collections.deque(), collections.deque()

        # Separate students into circular and square queues
        for student in students:
            if student == 0:
                circular.append(student)
            else:
                square.append(student)

        for sandwich in sandwiches:
            if sandwich == 0:
                if circular:
                    circular.popleft()
                else:
                    break  # No more circular sandwiches, break the loop
            else:
                if square:
                    square.popleft()
                else:
                    break  # No more square sandwiches, break the loop

        return len(circular) + len(square)


sol = Solution()
print(sol.countStudents([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1]))
