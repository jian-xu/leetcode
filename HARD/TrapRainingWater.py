class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r, min_h, rain = 0, len(height) - 1, 0, 0
        while(l < r):
            while(l < r and height[l] <= min_h):
                rain += min_h - height[l]
                l += 1
            while(r > l and height[r] <= min_h):
                rain += min_h - height[r]
                r -= 1
            min_h = min(height[l], height[r])
        return rain
