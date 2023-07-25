from typing import List,  Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]):
        if root is None:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        if left > right:
            return left + 1
        else:
            return right + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        stack = []
        stack.append(root)
        while len(stack) > 0:
            tmp = stack.pop()
            leftDepth = self.maxDepth(tmp.left)
            rightDepth = self.maxDepth(tmp.right)
            if leftDepth - rightDepth > 1 or rightDepth - leftDepth > 1:
                return False
            if tmp.right is not None:
                stack.append(tmp.right)
            if tmp.left is not None:
                stack.append(tmp.left)
        return True
             