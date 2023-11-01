class Solution:
    # Function to initialize the global variables.
    def setup(self):
        global v
        v = [[0 for i in range(100)] for j in range(100)]
        global ans
        ans = []

    # Function to find all paths from top-left to bottom-right.
    def path(self, arr, x, y, pth, n):
        if x == n - 1 and y == n - 1:
            global ans
            ans.append(pth)
            return
        global v
        if arr[x][y] == 0 or v[x][y] == 1:
            return
        v[x][y] = 1
        if x > 0:
            self.path(arr, x - 1, y, pth + "U", n)
        if y > 0:
            self.path(arr, x, y - 1, pth + "L", n)
        if x < n - 1:
            self.path(arr, x + 1, y, pth + "D", n)
        if y < n - 1:
            self.path(arr, x, y + 1, pth + "R", n)
        v[x][y] = 0

    # Function to find all possible paths from top-left to bottom-right.
    def findPath(self, m, n):
        global ans
        ans = []

        # if top-left or bottom-right position is blocked, return empty list.
        if m[0][0] == 0 or m[n - 1][n - 1] == 0:
            return ans

        # initialize global variables.
        self.setup()

        # find all possible paths from top-left to bottom-right.
        self.path(m, 0, 0, "", n)

        # sorting the paths lexicographically.
        ans.sort()

        # returning the sorted paths.
        return ans
