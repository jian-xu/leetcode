class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if (needle == ""):
            return 0
        needlelen = len(needle)

        for n in range(len(haystack) - needlelen + 1):
            if (haystack[n : (n+len(needle))] == needle):
                return n
        return -1

