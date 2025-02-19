from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # iterative
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        stack = [root]
        inorderIndex = 0
        for i in range(1, len(preorder)):
            preorderVal = preorder[i]
            node = stack[-1]
            if node.val != inorder[inorderIndex]:
                node.left = TreeNode(preorderVal)
                stack.append(node.left)
            else:
                while stack and stack[-1].val == inorder[inorderIndex]:
                    node = stack.pop()
                    inorderIndex += 1
                node.right = TreeNode(preorderVal)
                stack.append(node.right)
        return root
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # recursive
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        inorderIndex = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:1+inorderIndex], inorder[:inorderIndex])
        root.right = self.buildTree(preorder[1+inorderIndex:], inorder[inorderIndex+1:])
        return root
# time: O(n)
# space: O(n)