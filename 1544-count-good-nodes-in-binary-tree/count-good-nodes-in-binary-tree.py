# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        def checkNodes(node, maxNum):
            if not node:
                return 0

            res = 1 if node.val >= maxNum else 0
            maxNum = max(maxNum, node.val)
            res += checkNodes(node.left, maxNum)
            res += checkNodes(node.right, maxNum)
            return res
        
        return checkNodes(root,root.val)