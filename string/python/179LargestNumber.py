from functools import cmp_to_key
from typing import *


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Custom comparison function to sort numbers as strings in descending order
        def compare(x, y):
            xy = int(x + y)
            yx = int(y + x)
            return 1 if xy < yx else (-1 if xy > yx else 0)

        # Convert numbers to strings and sort them using the custom comparison function
        sorted_nums = sorted(map(str, nums), key=cmp_to_key(compare))

        # Join the sorted strings to form the largest number
        largest_num = "".join(sorted_nums)

        # Handle case where the largest number is 0
        return largest_num if largest_num[0] != "0" else "0"


sol = Solution()
print(sol.largestNumber([10, 2]))
