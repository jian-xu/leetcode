class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, s, path, res):
        if not s:
            res.append(path)
            return
        for i in range(1, len(s)+1):
            if self.ispal(s[:i]):
                self.dfs(s[i:], path+[s[:i]], res)

    def ispal(self, s):
        return s == s[::-1]

    """
    #once again, this is my complicated time exceeding solution
        if s == '':
            return 0
        instance, result = [], []
        for i in range(len(s)):
            instance.append(s[i])
        result.append(instance)
        tmp = []
        tmp.append(instance)
        while(True):
            for row in tmp:
                for i in range(0, len(row) - 1):
                    if self.ispalindrome(row[i] + row[i + 1]):
                        instance = row[0:i] + [row[i] + row[i + 1]] + row[i + 2:]
                        if instance not in result:
                            result.append(instance)
                        tmp.append(instance)
                for i in range(1, len(row) - 1):
                    if self.ispalindrome(row[i-1] + row[i] + row[i+1]):
                        instance = row[0:i - 1] + [row[i-1] + row[i] + row[i + 1]] + row[i + 2:]
                        if instance not in result:
                            result.append(instance)
                        tmp.append(instance)
                tmp.pop(0)
                break
            if tmp == []:
                return result

    def ispalindrome(self, s):
        return s == s[::-1]
    """
