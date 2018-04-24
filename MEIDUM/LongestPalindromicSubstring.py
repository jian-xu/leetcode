class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        #palindrome can be expanded from its center, and there are only 2n−1 such centers
        start = end = 0
        for i in range(len(s)):
            len1 = self.extend_around_center(s, i, i)
            len2 = self.extend_around_center(s, i, i + 1)
            # print(len1, len2)
            length = max(len1, len2)
            # print(length)
            if length > end - start:
                start = i - (length - 1) // 2
                end = i + length // 2
        return s[start:end + 1]

    @staticmethod
    def extend_around_center(s, l, r):
        left, right = l, r
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # 为什么要减一，因为结束之后，左右都各自加一或者减一了
        return right - left - 1