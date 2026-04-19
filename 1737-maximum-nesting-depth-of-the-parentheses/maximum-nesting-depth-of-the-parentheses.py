class Solution:
    def maxDepth(self, s: str) -> int:
        openP = 0
        maxOpen = 0
        for c in s:
            if c == "(":
                openP += 1
            if c == ")":
                openP -= 1
            maxOpen = max(openP,maxOpen)
        return maxOpen