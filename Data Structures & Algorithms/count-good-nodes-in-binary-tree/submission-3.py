# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        if not root:
            return []

        q = deque([(root, root.val)])

        max_val = 0

        res = 0

        while q:
            level_size = len(q)
            level = []

            for _ in range(level_size):
                
                node, max_val = q.popleft()

                if node.val >= max_val:
                    res += 1
                
                max_val = max(node.val, max_val)

                if node.left:
                    q.append((node.left, max_val))
                
                if node.right:
                    q.append((node.right, max_val))

        
        return res
        