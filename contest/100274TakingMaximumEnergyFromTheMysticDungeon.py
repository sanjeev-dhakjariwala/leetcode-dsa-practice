from typing import *


class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        max_energy = float("inf")
        n = len(energy)
        for i in range(n):
            ener = 0
            for j in range(i, n, k):
                ener += energy[j]
            max_energy = max(max_energy, ener)

        return max_energy

sol = Solution()
energy = [5, 2, -10, -5, 1]
print(sol.maximumEnergy(energy, 3))