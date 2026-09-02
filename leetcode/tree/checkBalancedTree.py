class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.getHeight(root) != -1

    def getHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)
        if leftHeight == -1 or rightHeight == -1:
            return -1
        if abs(leftHeight - rightHeight) > 1:
            return -1
        return 1 + max(leftHeight, rightHeight)
