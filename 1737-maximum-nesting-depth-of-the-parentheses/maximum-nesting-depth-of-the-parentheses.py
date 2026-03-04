class Solution(object):
    def maxDepth(self, s):
        currCount = 0
        maxCount = 0 
        for char in s:
            if char == '(':
                currCount += 1
                maxCount = max(maxCount, currCount)
            elif char == ')':
                currCount -= 1
        return maxCount