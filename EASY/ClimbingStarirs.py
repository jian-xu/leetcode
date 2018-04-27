'''递归啊，超时啊，尴尬啊
    class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = 0
        result = 0
        while(n - 2 * x >= 0):
            result += count(x, n - 2 * x)
            x += 1
        return result

def count(x, y):
    if (x == 0 or y == 0):
        return 1
    if (x == 1 or y == 1):
        return max(x, y)+ 1
    return count(x - 1, y) + count(x, y - 1)'''

class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = [1 for i in range(n+1)]
        for i in range(2, n + 1):
            result[i] = result[i - 1] + result[i - 2]
        return result[n]
    #fibonacci