# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
            if not root: return []
            if not root.left and not root.right: return [str(root.val)]
            return [str(root.val) + '->' + i for i in self.binaryTreePaths(root.left)] + [str(root.val) + '->' + i for i in self.binaryTreePaths(root.right)]
        