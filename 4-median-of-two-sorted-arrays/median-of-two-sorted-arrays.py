class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):  
        mList = nums1 + nums2
        mList.sort()
        median = (len(nums1) + len(nums2)) // 2
        if (len(nums1) + len(nums2)) % 2 == 0:
            return float((mList[median - 1] + mList[median])) / 2
        else:
            return float(mList[median])
