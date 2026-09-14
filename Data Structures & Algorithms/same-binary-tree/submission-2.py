# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        self.same = True

        def dfs(p, q):

            if not p and not q:
                return 0
            elif (p and not q) or (q and not p):
                self.same = False
            elif p.val != q.val:
                self.same = False
            
            if p and q:
                dfs(p.left, q.left)
                dfs(p.right, q.right)
            
        
        dfs(p,q)

        return self.same
            


        