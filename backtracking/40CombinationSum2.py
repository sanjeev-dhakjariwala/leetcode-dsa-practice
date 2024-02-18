class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)

        def helper(start, temp, s):
            if s == 0:
                res.append(temp[:])
                return
            if s < 0:
                return

            for i in range(start, n):
                temp.append(c)
                helper(start + 1, temp, s - c)
                temp.pop()

        helper([], target)
        return res
