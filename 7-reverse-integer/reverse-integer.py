class Solution(object):
    def reverse(self, x):
        reverse_int = int(str(abs(x))[::-1])
        if x < 0:
            reverse_int =reverse_int * -1
        if -2**31 <= reverse_int <= 2**31 -1:
            return reverse_int
        return 0