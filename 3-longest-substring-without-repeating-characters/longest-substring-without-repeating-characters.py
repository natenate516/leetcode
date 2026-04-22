class Solution(object):
    def lengthOfLongestSubstring(self, s):
        window = set()
        maxSize = 0
        l = 0
        for i in range(len(s)):
            while s[i] in window:
                window.remove(s[l])
                l += 1
            window.add(s[i])
            maxSize = max(i - l + 1, maxSize)
        return maxSize
        