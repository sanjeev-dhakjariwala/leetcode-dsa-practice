class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 0, x + 1
        while low <= high:
            mid = low + (high- low) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                low = mid + 1
            else:
                high = mid - 1
        return high

sol = Solution()
print(sol.mySqrt(8))