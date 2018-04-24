class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if (s == '' or len(s) % 2 != 0 or s[0] == ')' or s[0] == ']' or s[0] == '}'):
            return False
        tmp = []
        for i in range(len(s)):
            if (s[i] == '(' or s[i] == '[' or s[i] == '{'):
                tmp.append(s[i])
            elif (s[i] == ')' and tmp[-1] == '('):
                tmp.pop()
            elif (s[i] == ']' and tmp[-1] == '['):
                tmp.pop()
            elif (s[i] == '}' and tmp[-1] == '{'):
                tmp.pop()
            else:
                return False
        return False if (tmp != []) else True


def isValid(s):
    if (s == '' or len(s) % 2 != 0 or s[0] == ')' or s[0] == ']' or s[0] == '}'):
        return False
    tmp = []
    for i in range(len(s)):
        if (s[i] == '(' or s[i] == '[' or s[i] == '{'):
            tmp.append(s[i])
        elif (s[i] == ')' and tmp[-1] == '('):
            tmp.pop()
        elif (s[i] == ']' and tmp[-1] == '['):
            tmp.pop()
        elif (s[i] == '}' and tmp[-1] == '{'):
            tmp.pop()
        else:
            return False
    return False if (tmp != []) else True


