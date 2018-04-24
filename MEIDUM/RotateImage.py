import copy
class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        tmp = copy.deepcopy(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix) - 1, -1, -1):
                matrix[i][len(matrix) - 1 - j] = tmp[j][i]

        #one line solution
        #matrix[::] = zip(*matrix[::-1])