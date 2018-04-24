class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if (s == ''):
            return 0
        if (len(s) == 1 and s != ' '):
            return 1
        a = 0
        for i in range(len(s) - 1, -1, -1):
            if (s[i] == ' ' and a == 0):
                return a
            elif (s[i] == ' '):
                break
            a += 1
        return a