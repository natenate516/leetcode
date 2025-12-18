class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        countS = {}
        countT = {}
        for index in range(len(s)):
            countS[s[index]] = countS.get(s[index],0) + 1
            countT[t[index]] = countT.get(t[index],0) + 1
        return countS == countT