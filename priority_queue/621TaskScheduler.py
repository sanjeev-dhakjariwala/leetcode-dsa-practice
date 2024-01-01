from typing import *


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count the frequency of each task
        task_counts = {}

        for task in tasks:
            task_counts[task] = 1 + task_counts.get(task, 0)

        # Sort tasks by frequency in descending order
        sorted_tasks = sorted(task_counts.values(), reverse=True)

        # Get the maximum frequency
        max_frequency = sorted_tasks[0]

        # Count the number of tasks with the maximum frequency
        max_count = sorted_tasks.count(max_frequency)

        # Calculate the total time needed to finish all tasks
        total_time = (max_frequency - 1) * (n + 1) + max_count

        # If the total time is less than the length of tasks, return the length of tasks
        return max(total_time, len(tasks))


sol = Solution()
print(sol.leastInterval(["A", "A", "A", "B", "B", "B"], 2))
