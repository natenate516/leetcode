class Solution(object):
    def twoSum(self, nums, target):
        difference = {}
        for index, num in enumerate(nums):
            dif = target - num
            if dif in difference:
                return [difference[dif], index]
            difference[num] = index
        