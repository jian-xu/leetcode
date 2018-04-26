class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        """
        #dynamic programming --> top down
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j > 0 and j < i:
                    triangle[i][j] += min(triangle[i-1][j], triangle[i-1][j-1])
                elif j == 0:
                    triangle[i][j] += triangle[i-1][j]
                else:
                    triangle[i][j] += triangle[i-1][j-1]
        return min(triangle[-1])
        """
        """
        #bottom up, avoid the relatively rare instance, more concise
        f = [0] * (len(triangle) + 1)
        for row in triangle[::-1]:
            for i in range(len(row)):
                f[i] = row[i] + min(f[i], f[i+1])
        return f[0]
        """
        #my revised bottom up solusion
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]