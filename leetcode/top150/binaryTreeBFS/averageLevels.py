from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            size = len(stack)
            total = 0
            for i in range(size):
                node = stack.pop(0)
                total += node.val
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            res.append(total / size)
        return res