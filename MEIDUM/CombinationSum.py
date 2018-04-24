class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        re = []

        def dfs(candidates, target, select=[], last=0):
            if (target in candidates and target >= last):
                re.append(select + [target])
            #[dfs(candidates, target - i, select + [i], i) for i in candidates if (target - i > 0 and i >= last)]
            for i in candidates:
                if(target - i > 0 and i >= last):
                    dfs(candidates, target - i, select + [i], i)

        dfs(candidates, target)
        return re
