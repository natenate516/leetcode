class Solution(object):
    def strStr(self, haystack, needle):
        fst = len(haystack)
        snd = len(needle)
        if snd == 0:
            return 0
        
        i = 0
        while i < fst:
            nIndex = 0
            j = i
            while j < fst and nIndex < snd and haystack[j] == needle[nIndex]:
                j += 1
                nIndex += 1
            if nIndex == snd:
                return i
            i += 1
        return -1