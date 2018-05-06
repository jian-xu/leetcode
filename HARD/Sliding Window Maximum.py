class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums: return []
        ans = []
        cur_max = None
        for i in range(len(nums) - k + 1):
            if cur_max == None:
                cur_max = max(nums[i:i + k])
            else:
                if nums[i + k - 1] >= cur_max:
                    cur_max = nums[i + k - 1]
                elif cur_max > nums[i - 1]:
                    pass
                else:
                    cur_max = max(nums[i:i + k])
            ans += cur_max,
        return ans
