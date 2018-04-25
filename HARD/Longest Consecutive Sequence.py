class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        if nums == []:
            return 0
        nums = sorted(nums)
        a = nums[0]
        max_length = 1
        tmp = 1
        for i in range(1, len(nums)):
            if nums[i] == a + 1:
                tmp += 1
                a = nums[i]
            elif nums[i] == a:
                pass
            else:
                max_length = max(max_length, tmp)
                a = nums[i]
                tmp = 1
        max_length = max(max_length, tmp)
        return max_length
        """
        #more consice solution using set
        #attention: when it comes to negative numbers, set() would not return a sorted set, so you need to do some extra operation
        if nums == []:
            return 0
        nums = sorted(list(set(nums)))
        a = nums[0]
        tmp = 1
        max_length = 1
        for i in range(1, len(nums)):
            if nums[i] == a + 1:
                tmp += 1
            else:
                max_length = max(max_length, tmp)
                tmp = 1
            a = nums[i]
        max_length = max(max_length, tmp)
        return max_length
