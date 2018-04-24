def lengthOfLongestSubstring(s):
    tem = {}
    start = 0
    max_ = 0
    for a in range(len(s)):
        if s[a] in tem and start <= tem.get(s[a]):
            start = tem.get(s[a]) + 1
        else:
            max_ = max(max_, a - start + 1)
        tem[s[a]] = a
    return max_

s = 'abcadbcbb'
print(lengthOfLongestSubstring(s))