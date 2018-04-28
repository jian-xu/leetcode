class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return 0
        c = [s[i] for i in range(len(s))]
        res = 0
        for i in c:
            res = res*26 + (ord(i) - 64)
        return res