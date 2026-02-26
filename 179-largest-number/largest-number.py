class Solution(object):
    def largestNumber(self, nums):
        nums = self.mergeSort(nums, 0, len(nums) - 1)

        return str(int("".join(map(str, nums))))
    
    def mergeSort(self, nums, l, r):
        if l > r:
            return 
        if l == r:
            return [nums[l]]

        mid = l + (r-l)//2

        left = self.mergeSort(nums, l, mid)
        right = self.mergeSort(nums, mid + 1, r)

        return self.merge(left, right)

    def merge(self, list1, list2):
        res = []
        i = 0
        j = 0

        while i < len(list1) and j < len(list2):
            if str(list1[i]) + str(list2[j]) < str(list2[j]) + str(list1[i]):
                res.append(list2[j])
                j += 1
            else:
                res.append(list1[i])
                i += 1
        
        res.extend(list1[i:] or list2[j:])

        return res
        