class Solution:
    def minimumChairs(self, s: str) -> int:
        chair = 0
        max_chair = float('-inf')

        for i in s:
            if i == 'E':
                chair += 1
            else:
                chair -= 1
            max_chair = abs(max(max_chair, chair))
        
        return max_chair

sol = Solution()
s = "ELEELEELLL"
print(sol.minimumChairs(s))