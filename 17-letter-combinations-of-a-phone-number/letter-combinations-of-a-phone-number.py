class Solution(object):
    def letterCombinations(self, digits):
        if digits == '': return []
        letters = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        solution = ['']

        for d in digits:
            solution = [x + ch for x in solution for ch in letters[int(d)]]

        return solution