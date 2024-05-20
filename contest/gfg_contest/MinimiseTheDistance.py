from typing import List


class Solution:
    def minimumDis(self, N: int, X: List[int]) -> int:
        # code here
        if N == 1:
            return X[0]
        min_dis = float("inf")

        for i in range(N):
            dist = 0
            for j in range(N):
                dist += abs(X[i] - X[j])
                print(i , j)
            min_dis = min(min_dis, dist)

        return min_dis


sol = Solution()
N = 3
X = [3, 2, 2]
print(sol.minimumDis(N, X))
"""
0 0
0 1
0 2
1 0
1 1
1 2
2 0
2 1
2 2
1
"""
