class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mini = nums[0]
        for i in range(len(nums)):
            if(nums[i] > 0):
                break
            mini = max(mini, nums[i])
            if(i == len(nums) - 1):
                return mini
        maxsofar = maxfinal =0
        for i in range(len(nums)):
            maxsofar += nums[i]
            if maxsofar < 0:
                maxsofar = 0
            maxfinal = max(maxfinal, maxsofar)

        return maxfinal
        #return recursive(nums, 0, len(nums) - 1)
def recursive(X, l, r):
    if (l > r):
        return 0
    elif (l == r):
        return max(X[l], 0)
    m = (l + r) // 2
    lmax, lsum = 0, 0
    rmax, rsum = 0, 0
    for i in range(m, l, -1):
        lsum += X[i]
        lmax = max(lmax, lsum)
    for i in range(m, r):
        rsum += X[i]
        rmax = max(rmax, rsum)
    return max(rmax + lmax, recursive(X, l, m), recursive(X, m + 1, r)) if ((l + r) % 2==1) else max(rmax + lmax + X[m], recursive(X, l, m), recursive(X, m + 1, r))