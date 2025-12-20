class Solution(object):
    def hammingWeight(self, n):
        total = 0
        while n:
            total += n % 2
            n = n >> 1
        return total