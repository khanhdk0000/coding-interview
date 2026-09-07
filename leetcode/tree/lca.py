# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.dfs(root, p, q)
        return lca
    
    def dfs(self, node, p, q):
        global lca
        if not node:
            return False
        node_is_p_or_q = node == p or node == q
        left_has_p_or_q = self.dfs(node.left, p, q)
        right_has_p_or_q = self.dfs(node.right, p, q)
        if (node_is_p_or_q + left_has_p_or_q + right_has_p_or_q) == 2:
            lca = node
        return (
            node_is_p_or_q or left_has_p_or_q or right_has_p_or_q
        )