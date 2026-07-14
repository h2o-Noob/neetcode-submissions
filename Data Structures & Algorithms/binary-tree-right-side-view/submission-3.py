# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        q = collections.deque([root])
        res = []
        if not root:
            return []

        def dp(root):

            while q:
                level_size = len(q)

                for i in range(level_size):
                    node = q.popleft()
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                    if i == level_size - 1:
                        res.append(node.val)
        dp(root)

        return res

        