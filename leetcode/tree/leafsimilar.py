# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        lst1 = self.getLeaves(root1)
        lst2 = self.getLeaves(root2)
        # print(lst1)
        print(lst1, lst2)
        return lst1 == lst2

    # def getLeaves(self, root):
    #     if root is None:
    #         return []
    #     if root.left is None and root.right is None:
    #         return [root.val]
    #     left_leaves = self.getLeaves(root.left)
    #     right_leaves = self.getLeaves(root.right)
    #     return left_leaves + right_leaves
    def getLeaves(self, root):
        stack = []
        stack.append(root)
        leaves = []
        while stack:
            node = stack.pop()
            if node.left is None and node.right is None:
                leaves.append(node.val)
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
        return leaves
            