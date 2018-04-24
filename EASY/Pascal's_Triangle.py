class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        res = [[] for i in range(numRows)]
        res[0] = [1]
        res[1] = [1, 1]
        for i in range(2, len(res)):
            res[i].append(1)
            for j in range(1, i):
                res[i].append(res[i-1][j-1] + res[i-1][j])
            res[i].append(1)
        return res
