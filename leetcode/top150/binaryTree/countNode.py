from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [root]
        total = 0
        while stack:
            node = stack.pop()
            total += 1
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return total
# time: O(n)
# space: O(n)