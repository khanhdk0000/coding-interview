from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # check if the given tree is a valid binary search tree
        # inorder traversal
        # left -> root -> right
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        inorder_list = inorder(root)
        for i in range(1, len(inorder_list)):
            if inorder_list[i] <= inorder_list[i-1]:
                return False
        return True