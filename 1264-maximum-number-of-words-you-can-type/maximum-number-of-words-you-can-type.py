class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        strs = text.split()
        letters = []
        for c in brokenLetters:
            letters.append(c)
        n = len(strs)
        for word in strs:
            for c in word:
                if c in letters:
                    n -= 1
                    break 
        
        return n