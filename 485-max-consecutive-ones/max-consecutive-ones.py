class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        maxCount = 0
        localCount = 0
        for i in nums:
            if i == 1:
                localCount +=1
            else:
                localCount = 0
            maxCount = max(maxCount,localCount)
        return maxCount
