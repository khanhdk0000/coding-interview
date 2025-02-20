from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        stack = [(root, targetSum - root.val)]
        while stack:
            node, target = stack.pop()
            if not node.left and not node.right and target == 0:
                return True
            if node.left:
                stack.append((node.left, target - node.left.val))
            if node.right:
                stack.append((node.right, target - node.right.val))
        return False
# time: O(n)
# space: O(n)