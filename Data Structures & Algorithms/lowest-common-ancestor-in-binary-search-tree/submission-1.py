# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        while root:
            if root.val <= max(p.val, q.val) and root.val >= min(p.val, q.val):
                return root
            elif root.val <= q.val and root.val <= p.val:
                root = root.right
            else:
                root = root.left

