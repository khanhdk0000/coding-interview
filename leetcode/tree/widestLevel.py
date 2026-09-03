from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return []
        queue = deque([(root, 0)])
        res = 1
        while queue:
            level_size = len(queue)
            leftmost_idx = queue[0][1]
            rightmost_idx = leftmost_idx
            for _ in range(level_size):
                node, i = queue.popleft()
                if node.left:
                    queue.append((node.left, 2*i + 1))
                if node.right:
                    queue.append((node.right, 2*i + 2))
                rightmost_idx = i
            res = max(res, rightmost_idx - leftmost_idx + 1)
        return res