from typing import *


class Solution:
    def tournamentWinner(self, competitions, results):
        hash_set = {}

        for i in range(len(competitions)):
            for j in range(len(competitions[0])):
                hash_set[competitions[i][j]] = 0
        i = 0
        for competition in competitions:
            temp_res = results[i]
            if temp_res == 0:
                hash_set[competition[1]] = 3 + hash_set.get(competition[1], 0)
            else:
                hash_set[competition[0]] = 3 + hash_set.get(competition[0], 0)
            i += 1
        max_point = float("-inf")
        ans = ""
        for key, values in hash_set.items():
            if max_point < values:
                max_point = values
                ans = key
        print(hash_set)
        return ans


sol = Solution()
print(
    sol.tournamentWinner(
        [
            ["HTML", "C#"],
            ["C#", "Python"],
            ["HTML", "Python"],
        ],
        [0, 0, 1],
    )
)
