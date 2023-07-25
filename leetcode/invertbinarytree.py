from typing import List,  Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        stack = []
        stack.append(root)
        while len(stack) > 0:
            tmp = stack.pop()
            if tmp.right is not None and tmp.left is not None:
                stack.append(tmp.right)
                stack.append(tmp.left)
                tmpVal = tmp.left
                tmp.left = tmp.right
                tmp.right = tmpVal
            elif tmp.left is not None and tmp.right is None:
                stack.append(tmp.left)
                tmpVal = tmp.left
                tmp.left = tmp.right
                tmp.right = tmpVal
            elif tmp.right is not None and tmp.left is None:
                stack.append(tmp.right)
                tmpVal = tmp.right
                tmp.right = tmp.left
                tmp.left = tmpVal
        return root


