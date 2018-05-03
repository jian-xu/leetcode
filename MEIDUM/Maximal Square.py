class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        """
        #this is my brutal force solution, yeah, it's stupid
        if matrix == []:
            return 0
        res = 0
        if '1' in [j for i in matrix for j in i]:
            res = 1
        m, n = len(matrix), len(matrix[0])
        dp = [[int(j) for j in i[:]]for i in matrix[:]]
        i, j = 0, 0
        while(i < m):
            tmp = 0
            j = 0
            while(j < n):
                if dp[i][j] == 1:
                    tmp += 1
                else:
                    tmp = 0
                if tmp**2 > res:
                    if i+tmp <= m and sum(b for a in dp[i:i+tmp] for b in a[j-tmp+1:j+1]) == tmp**2:
                        res = tmp**2
                    else:
                        tmp -= 1
                j += 1
            i += 1
        return res
        """
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0 if matrix[i][j] == '0' else 1 for j in range(n)] for i in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    # attention please, here is the trick
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                else:
                    dp[i][j] = 0
        ans = max([max(i) for i in dp])
        return ans ** 2