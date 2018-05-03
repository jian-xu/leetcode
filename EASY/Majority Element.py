class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        for i in nums:
            if nums.count(i)/len(nums) > 0.5:
                return i
        return None
        """
        nums = sorted(nums)
        return nums[len(nums)//2]