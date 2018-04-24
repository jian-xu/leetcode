class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        re = []
        def dfs(candidates, select=[]):
            if (not candidates):
                if (select not in re):
                    re.append(select)
            for i in range(len(candidates)):
                dfs(candidates[:i] + candidates[i + 1:], select + [candidates[i]])

        dfs(nums)
        return re
