from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # iterative
        if not inorder or not postorder:
            return None
        root = TreeNode(postorder[-1])
        stack = [root]
        inorderIndex = len(inorder) - 1
        for i in range(len(postorder)-2, -1, -1):
            postorderVal = postorder[i]
            node = stack[-1]
            if node.val != inorder[inorderIndex]:
                node.right = TreeNode(postorderVal)
                stack.append(node.right)
            else:
                while stack and stack[-1].val == inorder[inorderIndex]:
                    node = stack.pop()
                    inorderIndex -= 1
                node.left = TreeNode(postorderVal)
                stack.append(node.left)
        return root
# time: O(n)
# space: O(n)