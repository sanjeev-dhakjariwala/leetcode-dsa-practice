from typing import *


class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        n1 = len(energyDrinkA)
        n2 = len(energyDrinkB)
        # energyDrinkA.sort()
        # energyDrinkB.sort()
        if sum(energyDrinkA) == sum(energyDrinkB):
            return sum(energyDrinkA)
        i = 1
        j = 1
        res = []
        curr = ""
        if energyDrinkA[0] > energyDrinkB[0]:
            curr = "A"
            res.append(energyDrinkA[0])
        elif energyDrinkA[0] < energyDrinkB[0]:
            curr = "B"
            res.append(energyDrinkB[0])
        else:
            curr = "A"
            res.append(energyDrinkA[0])

        while i < n1 and j < n2:
            if energyDrinkA[i] == energyDrinkB[j]:
                curr = "A"
                res.append(energyDrinkA[i])
            elif energyDrinkA[i] > energyDrinkB[j]:
                if curr == "A":
                    res.append(energyDrinkA[i])
                else:
                    #res.pop()
                    #res.append(energyDrinkB[j])
                    curr = "B"
            else:
                if curr == "A":
                    #res.pop()
                    #res.append(energyDrinkB[j])
                    curr = "B"

                else:
                    res.append(energyDrinkA[i])
            i += 1
            j += 1

        return sum(res)


sol = Solution()
energyDrinkA = [4, 1, 1]
energyDrinkB = [1, 1, 3]
""" energyDrinkA = [1, 3, 1]
energyDrinkB = [3, 1, 1] """
""" energyDrinkA = [2, 4, 6, 8, 10]
energyDrinkB = [1, 3, 5, 7, 9] """
# energyDrinkA = [5, 1, 5, 1, 5]
# energyDrinkB = [1, 5, 1, 5, 1]
print(sol.maxEnergyBoost(energyDrinkA, energyDrinkB))
