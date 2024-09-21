from typing import *


class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        c = 0
        n = len(batteryPercentages)
        for i in range(n):
            if batteryPercentages[i] > 0:
                c += 1
            else:
                continue
            for j in range(i + 1, n):
                if batteryPercentages[j] == 0:
                    continue
                else:
                    batteryPercentages[j] -= 1
        return c


sol = Solution()
print((sol.countTestedDevices([1, 1, 2, 1, 3])))
