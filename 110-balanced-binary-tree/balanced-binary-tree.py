# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        if not root:
            return True

        leftHeight = self.checkHeight(root.left)
        rightHeight = self.checkHeight(root.right)

        if abs(leftHeight - rightHeight) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)

    def checkHeight(self, root):
        if not root:
            return 0
        leftSide = self.checkHeight(root.left) + 1
        rightSide = self.checkHeight(root.right) + 1
        return max(leftSide, rightSide)