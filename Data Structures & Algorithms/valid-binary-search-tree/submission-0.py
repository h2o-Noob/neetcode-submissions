# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        minn = float('-inf')
        maxx = float('inf')

        def dfs(root, minn, maxx):

            if not root:
                return True
            
            return minn < root.val < maxx and dfs(root.left, minn, root.val) and dfs(root.right, root.val, maxx)
        
        return dfs(root, minn, maxx)
        



        