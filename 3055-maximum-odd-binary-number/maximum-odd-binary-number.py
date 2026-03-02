class Solution(object):
    def maximumOddBinaryNumber(self, s):
        ones = 0
        for c in s:
            if c == '1':
                ones += 1
        
        maxOdd = ""
        for i in range(len(s)):
            if ones == 1 and i == len(s) - 1:
                maxOdd += '1'
                break
            elif ones > 1:
                maxOdd += '1'
                ones -= 1
            else:
                maxOdd += '0'
        return maxOdd