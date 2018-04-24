import copy
class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # this solution is kind of tricky and the spotlight is on
        # 'for j in range(len(res) - l, len(res))' , this place restrict the
        # succeeding operation on res
        res = [[]]
        nums.sort()
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                l = len(res)
            for j in range(len(res) - l, len(res)):
                res.append(res[j] + [nums[i]])
        return res
        """
        res = [[]]
        for num in sorted(nums):
            #tmp = copy.deepcopy(res)
            #for item in tmp:
                #if ([item + [nums]] not in res):
                    #res += [item + [num]]
            res += [item + [num] for item in res]
            fool = []
            for i in res:
                if(i not in fool):
                    fool.append(i)
        return res
        """




