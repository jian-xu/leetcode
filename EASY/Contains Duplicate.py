class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums == []:
            return False
        nums = sorted(nums)
        tmp = nums[0]
        for i in nums[1:]:
            if i == tmp:
                return True
            tmp = i
        return False