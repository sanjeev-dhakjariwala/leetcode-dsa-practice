from typing import *


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        '''
        Brute force approach
        while True:
            changed = False
            for i in range(len(asteroids) - 1):
                if asteroids[i] > 0 and asteroids[i + 1] < 0:
                    if abs(asteroids[i]) == abs(asteroids[i + 1]):
                        asteroids.pop(i)
                        asteroids.pop(
                            i
                        )  # After the first pop, the next asteroid's index becomes i
                        changed = True
                        break
                    elif abs(asteroids[i]) > abs(asteroids[i + 1]):
                        asteroids.pop(i + 1)
                        changed = True
                        break
                    else:
                        asteroids.pop(i)
                        changed = True
                        break
            if not changed:
                break
            '''
        return asteroids


sol = Solution()
print(sol.asteroidCollision([5, 10, -5]))
