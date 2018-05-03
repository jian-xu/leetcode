class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # time limit exceeded but simple solution
        if nums == [] or len(nums) == 1:
            return nums
        nums = sorted(nums)
        tmp = nums[0]
        res = []
        if nums.count(tmp) * 3 > len(nums):
            res.append(tmp)
        for i in nums[1:]:
            if i != tmp:
                if nums.count(i) * 3 > len(nums):
                    res.append(i)
            tmp = i
        return res