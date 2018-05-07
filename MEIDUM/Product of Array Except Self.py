class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        left, right = [0] * len(nums), [0] * len(nums)
        left[0] = nums[0]
        right[-1] = nums[-1]
        for i in range(1, len(nums)):
            left[i] = left[i-1] * nums[i]
        for i in range(len(nums) - 2, -1, -1):
            right[i] = right[i+1] * nums[i]
        res.append(right[1])
        for i in range(1, len(nums)-1):
            res.append(left[i-1] * right[i+1])
        res.append(left[-2])
        return res