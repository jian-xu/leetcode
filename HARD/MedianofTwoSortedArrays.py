class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        result = []
        while(nums1 and nums2):
            if (nums1[0] <= nums2[0]):
                result.append(nums1[0])
                nums1.pop(0)
            else:
                result.append(nums2[0])
                nums2.pop(0)
        while(nums1):
            result.append(nums1[0])
            nums1.pop(0)
        while(nums2):
            result.append(nums2[0])
            nums2.pop(0)
        if (len(result)%2 == 1):
            return result[len(result)//2] / 1
        else:
            return (result[len(result) // 2] + result[len(result) // 2 - 1]) / 2