class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)  # row
        n = len(grid[0])  # column
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
        for i in range(1, n):
            grid[0][i] += grid[0][i-1]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i][j-1], grid[i-1][j])
        return grid[-1][-1]

        """
        yeah, again, this is my stupid recursive solution
        start = [0, 0]
        target = [m - 1, n - 1]
        path = []
        def paths(a, b, c = 0):
            if (b[0] - a[0] == 0 and b[1] - a[1] == 0):
                path.append(c + grid[-1][-1])
            if (b[0] - a[0] >= 1):
                paths([(a[0] + 1), a[1]], b, c + grid[a[0]][a[1]])
            if (b[1] - a[1] >= 1):
                paths([a[0], (a[1] + 1)], b, c + grid[a[0]][a[1]])
        paths(start, target)
        return min(path)
        """
