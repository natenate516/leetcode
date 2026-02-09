# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def balanceBST(self, root):
        nodes = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            nodes.append(root)
            inorder(root.right)
            root.left = None
            root.right = None

        def rebuild(l, r):
            mid = (l + r) // 2
            if l > r: 
                return None
            root = nodes[mid]
            if mid != l: 
                root.left = rebuild(l, mid - 1)
            if mid != r: 
                root.right = rebuild(mid + 1, r)
            return root

        inorder(root)
        return rebuild(0, len(nodes) - 1)
        
        