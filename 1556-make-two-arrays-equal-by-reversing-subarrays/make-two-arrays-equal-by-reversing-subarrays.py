class Solution(object):
    def canBeEqual(self, target, arr):
        count={}
        for num in target:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        for num in arr:
            if num not in count or count[num] == 0:
                return False
            else:
                count[num] -= 1
        return True
        