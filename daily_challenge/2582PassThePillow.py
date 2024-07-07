class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        index = 1
        print(index, end="->")
        reverse = False
        i = 1
        while i <= time:
            if index < n and not reverse:
                index += 1
                print(index, end="->")
            elif index == 1:
                index += 1
                print(index, end="->")
                reverse = False
            else:
                index -= 1
                print(index, end="->")
                reverse = True
            i += 1

        return index


sol = Solution()
sol.passThePillow(4, 5)
# sol.passThePillow(18, 38)
