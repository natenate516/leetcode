class Solution(object):
    def reverseString(self, s):
        l = 0
        r = len(s) - 1
        while l < r:
            tmp = s[l]
            s[l] = s[r]
            s[r] = tmp
            l += 1
            r -= 1
        