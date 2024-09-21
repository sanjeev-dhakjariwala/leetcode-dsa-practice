from typing import *


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        for start in range(n):
            currentGas = 0
            success = True

            for i in range(n):
                station = (start + i) % n
                currentGas += gas[station] - cost[station]

                if currentGas < 0:
                    success = False
                    break

            if success:
                return start

        return -1

        """ n = len(gas)

        total_gas, current_gas, start_station = 0, 0, 0

        for i in range(n):
            total_gas += gas[i] - cost[i]
            current_gas += gas[i] - cost[i]

            if current_gas < 0:
                start_station = i + 1
                current_gas = 0

        return start_station if total_gas >= 0 else -1 """


sol = Solution()
print(sol.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
