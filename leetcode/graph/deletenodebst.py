from typing import List,  Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return root
        curr = root
        prev = None
        while (curr != None and curr.val != key):
            prev = curr
            if curr.val > key:
                curr = curr.left
            elif curr.val < key:
                curr = curr.right
        if curr == None:
            return root
        
        if curr.left is None or curr.right is None:
            newCurr = None
            if curr.left is None:
                newCurr = curr.right
            else:
                newCurr = curr.left

            if prev is None: # curr is root
                return newCurr

            if curr == prev.left:
                prev.left = newCurr
            else:
                prev.right = newCurr
            curr = None
        else:
            p = None
            temp = curr.right
            while(temp.left != None):
                p = temp
                temp = temp.left
            if p != None:
                p.left = temp.right
            else:
                curr.right = temp.right
            curr.val = temp.val
            temp = None
        return root