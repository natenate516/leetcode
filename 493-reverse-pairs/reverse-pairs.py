class Solution(object):
    def reversePairs(self, nums):
        def mergeSort(l, r):
            if l >= r:
                return 0
            m = (l+r) // 2
            count = mergeSort(l,m) + mergeSort(m+1,r)

            i = l
            j = m + 1
            while i <= m and j <= r:
                if nums[i] > 2 * nums[j]:
                    count += m - i + 1
                    j += 1
                else:
                    i += 1
            merge(nums, l, m, r)
            return count
        
        def merge(arr, l, m, r):
            n1 = m - l + 1
            n2 = r - m

            L = [0] * n1
            R = [0] * n2

            for i in range(n1):
                L[i] = arr[l + i]
            for j in range(n2):
                R[j] = arr[m + 1 + j]

            i = j = 0
            k = l

            while i < n1 and j < n2:
                if L[i] <= R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            while i < n1:
                arr[k] = L[i]
                i += 1
                k += 1
            while j < n2:
                arr[k] = R[j]
                j += 1
                k += 1

        return mergeSort(0, len(nums) - 1)

