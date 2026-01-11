class Solution(object):
    def searchInsert(self, nums, target):
        l = 0
        h = len(nums)
        while l < h:
            mid = (l + h) // 2
            if target > nums[mid]:
                l = mid + 1
            else:
                h = mid
        return l