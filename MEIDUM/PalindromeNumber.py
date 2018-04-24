class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        y = 0
        tmp = x
        d = 1
        while (x // 10 > 0):
            d += 1
            x //= 10
        x = tmp
        i = 0
        while (i < d // 2):
            y = x % 10 + 10 * y
            x //= 10
            i += 1
        if (d % 2 == 1):
            y = x % 10 + 10 * y
        return True if (x == y) else False


def isPalindrome(x):
    if x < 0:
        return False
    y = 0
    tmp = x
    d = 1
    while (x // 10 > 0):
        d += 1
        x //= 10
    x = tmp
    i = 0
    while (i < d//2):
        y = x % 10 + 10 * y
        x //= 10
        i += 1
    if (d % 2 == 1):
        y = x % 10 + 10 * y
    '''if (x == y):
        return True
    else:
        return False
    '''
    return True if (x == y) else False

print(isPalindrome(2367632))
