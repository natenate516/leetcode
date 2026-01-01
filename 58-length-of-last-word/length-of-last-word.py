class Solution(object):
    def lengthOfLastWord(self, s):
        x = len(s) - 1
        while s[x] == ' ':
            x -= 1
        count = 0
        while s[x] != ' ':
            if x >= 0:
                count += 1
                x -= 1
            else:
                break
        return count        
        