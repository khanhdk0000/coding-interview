from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # min difference between any two nodes in the tree

        # inorder traversal
        # left -> root -> right
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        inorder_list = inorder(root)
        min_diff = float('inf')
        for i in range(1, len(inorder_list)):
            min_diff = min(min_diff, inorder_list[i] - inorder_list[i-1])
        return min_diff