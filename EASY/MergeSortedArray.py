class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if (n == 0):
            return None
        if (m == 0):
            for s in range(n):
                nums1.append(nums2[s])
        i, j = 0, 0
        while(i < m and j < n):
            if (nums1[i] >= nums2[j]):
                nums1.insert(i, nums2[j])
                j += 1
                m += 1
            else:
                i += 1
        if (j < n):
            for s in range(j, n):
                nums1.insert(-1, nums2[s])
        return None

