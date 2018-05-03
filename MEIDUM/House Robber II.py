class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums and len(nums) < 4:
            return max(nums)
        def func(nums):
            last = now = 0
            for i in nums:
                last, now = now, max(last+i, now)
            return now
        return max(func(nums[:-1]), func(nums[1:]))