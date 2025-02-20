from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        stack = [root]
        zigzag = False
        while stack:
            size = len(stack)
            level = []
            for i in range(size):
                node = stack.pop(0)
                if zigzag:
                    level.insert(0, node.val)
                else:
                    level.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            res.append(level)
            zigzag = not zigzag
        return res