class Solution(object):
    def myAtoi(self, s):
        sign = 1
        l = 0
        while l < len(s) and s[l] == ' ':
            l += 1
        if l < len(s) and (s[l] == '-' or s[l]== '+'):
            if s[l] == '-':
                sign = -1
            l += 1
        n = l
        while n < len(s) and s[n].isnumeric():
            n+=1
        if l == n:
            return 0
        integer = int(s[l:n]) * sign

        if integer > 2**31 - 1:
            return 2**31 - 1
        elif integer < -2**31:
            return -2**31
        else:
            return integer
