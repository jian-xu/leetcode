import copy
class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        """
        #my stupid recursive solution
        re = []
        def func(a, b=[], c=[]):
            c = sorted(c)
            if (a == 0 and c not in re):
                re.append(c)
                return
            for i in b:
                tmp = copy.deepcopy(b)
                tmp.remove(i)
                func(a - 1, tmp, c + [i])

        for i in range(0, len(nums) + 1):
            func(i, nums)
        return re
        """
        """
        #someone's worked solution
        res = []
        def dfs(nums, index, path, res):
            res.append(path)
            for i in range(index, len(nums)):
                    dfs(nums, i+1, path+[nums[i]], res)
        dfs(nums, 0, [], res)
        return res
        """
        #excellent solution!!!!
        res = [[]]
        for num in sorted(nums):
            res += [item + [num] for item in res]
        return res

