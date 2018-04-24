class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        num_max = (1 << 31) - 1
        flag = -1 if x < 0 else 1
        y = 0
        if x < 0:
            x = abs(x)
            while (x != 0):
                y = x % 10 + 10 * y
                x = x // 10
        else:
            while (x != 0):
                y = x % 10 + 10 * y
                x = x // 10
        return 0 if (y > num_max) else y * flag


def reverse(x):
    num_max = (1 << 31) - 1
    flag = -1 if x < 0 else 1
    y = 0
    if x < 0:
        x = abs(x)
        while (x != 0):
            y = x % 10 + 10 * y
            x = x // 10
    else:
        while (x != 0):
            y = x % 10 + 10 * y
            x = x // 10
    return 0 if (y > num_max) else y * flag

print(reverse(120))
