class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        re = []
        tmp = []
        def dfs(candidates, select = []):
            if (not candidates):
                re.append(select)
            for i in range(len(candidates)):
                dfs(candidates[:i] + candidates[i + 1:], select + [i])

        dfs(nums)
        return re
