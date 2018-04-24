class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        """
        #this is my time-consuming recursive solution, which is bad
        start = [0, 0]
        target = [m-1, n-1]
        path = [0]
        def paths(a, b):
            if (b[0]-a[0]==0 and b[1]-a[1]==0):
                path[0] += 1
            if (b[0] - a[0] >= 1):
                paths([(a[0] + 1), a[1]], b)
            if (b[1] - a[1] >= 1):
                paths([a[0], (a[1] + 1)], b)
        paths(start, target)
        return path[0]
        """
        matrix = [[1 for i in range(n)] for i in range(m)]
        for i in range(1, n):
            for j in range(1, m):
                matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]
        return matrix[-1][-1]