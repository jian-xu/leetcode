class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(k, n, 1, [], res)
        return res

    def dfs(self, k, n, curr, arr, res):
        if len(arr) == k:
            if sum(arr) == n:
                res.append(list(arr))
        if len(arr) > k or curr > 9:
            return
        for i in range(curr, 10):
            arr.append(i)
            self.dfs(k, n, i + 1, arr, res)
            arr.pop()