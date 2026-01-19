class Solution(object):
    def reverseVowels(self, s):
        vowel =  {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        l = 0
        r = len(s) - 1
        word = list(s)
        while l < r:
            while l < r and not word[l] in vowel:
                l += 1
            
            while l < r and not word[r] in vowel:
                r -= 1

            word[l], word[r] = word[r], word[l]

            l +=1
            r -=1

        return "".join(word)
        