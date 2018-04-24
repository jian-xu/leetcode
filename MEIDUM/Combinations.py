class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        #start = list(range(1, n))
        re = []
        def func(a, b, c = []):
            if(b == 0):
                re.append(c)
                return
            for i in range(a - 1, 0, -1):
                func(a - 1, b - 1, c + [i])
        func(n, k)
        return re
