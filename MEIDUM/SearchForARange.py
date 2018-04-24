class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if(nums == []):
            return [-1, -1]
        n = len(nums)
        left, right = -1, -1
        l, r = 0, n-1
        while(l < r):
            m = (l + r) // 2
            if(nums[m] < target):
                l = m + 1
            else:
                r = m
        if(nums[l] != target):
            return [left, right]
        left = l
        l, r = left, n - 1
        while(l < r):
            m = (l + r)//2 + 1
            if(nums[m] == target):
                l = m
            else:
                r = m - 1
        right = l
        return [left, right]



        '''
        if(nums == []):
            return [-1, -1]
        if(len(nums) == 1):
            if(nums[0] == target):
                return [0, 0]
            else:
                return [-1,-1]
        start = end = -1
        middle = len(nums) // 2
        while(True):
            if(nums[middle] > target):
                middle = middle // 2
            elif(nums[middle] < target):
                middle = (len(nums) + middle) // 2
            elif(nums[middle] == target):
                start = end = middle
                if (middle == len(nums) - 1 or middle == 0):
                    return [start, end]
                while(0 <= end <= len(nums) - 1):
                    if(nums[end] != target):
                        end -= 1
                        break
                    if(end == len(nums) - 1):
                        break
                    end += 1
                while(len(nums) - 1 >= start >= 0):
                    if(nums[start] != target):
                        start += 1
                        break
                    if(start == 0):
                        break
                    start -= 1
                break
            if((middle == len(nums) - 1 and nums[0] != target) or (middle == 0 and nums[-1] != target)):
                break
        return [start, end]
        '''