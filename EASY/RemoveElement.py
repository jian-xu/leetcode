class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        j = 0
        while(val in nums):
            if (j <= (len(nums) - 1)):
                for i in range(j, len(nums)):
                    if (val == nums[i]):
                        nums.pop(i)
                        j = i
                        break
            else:
                return len(nums)
        return len(nums)


