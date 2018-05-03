class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        """
        a = nums[0:k]
        for i in nums[k:]:
            tmp = min(a)
            if i > tmp:
                a.remove(tmp)
                a.append(i)
        return min(a)
        """
        nums = sorted(nums)
        return nums[-k]