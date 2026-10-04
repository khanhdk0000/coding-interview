from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ---------- Preorder: root, left, right ----------

def preorder_recursive(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    return [root.val] + preorder_recursive(root.left) + preorder_recursive(root.right)


def preorder_iterative(root: Optional[TreeNode]) -> List[int]:
    res, stack = [], [root] if root else []
    while stack:
        node = stack.pop()
        res.append(node.val)
        # push right first so left pops first
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return res


# ---------- Inorder: left, root, right ----------

def inorder_recursive(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    return inorder_recursive(root.left) + [root.val] + inorder_recursive(root.right)


def inorder_iterative(root: Optional[TreeNode]) -> List[int]:
    res, stack, node = [], [], root
    while node or stack:
        while node:  # go as far left as possible
            stack.append(node)
            node = node.left
        node = stack.pop()
        res.append(node.val)
        node = node.right
    return res


# ---------- Postorder: left, right, root ----------

def postorder_recursive(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    return postorder_recursive(root.left) + postorder_recursive(root.right) + [root.val]


def postorder_iterative(root: Optional[TreeNode]) -> List[int]:
    # one stack + last-visited pointer: pop node only after its right subtree is done
    res, stack, node, last = [], [], root, None
    while node or stack:
        while node:
            stack.append(node)
            node = node.left
        peek = stack[-1]
        if peek.right and peek.right is not last:
            node = peek.right
        else:
            res.append(peek.val)
            last = stack.pop()
    return res


# ---------- Level order (BFS) ----------

def levelorder_recursive(root: Optional[TreeNode]) -> List[List[int]]:
    res = []

    def dfs(node, depth):
        if not node:
            return
        if depth == len(res):
            res.append([])
        res[depth].append(node.val)
        dfs(node.left, depth + 1)
        dfs(node.right, depth + 1)

    dfs(root, 0)
    return res


def levelorder_iterative(root: Optional[TreeNode]) -> List[List[int]]:
    res, q = [], deque([root] if root else [])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(level)
    return res


if __name__ == "__main__":
    #        1
    #      /   \
    #     2     3
    #    / \     \
    #   4   5     6
    #      /
    #     7
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(7))), TreeNode(3, None, TreeNode(6)))

    for rec, it, expected in [
        (preorder_recursive, preorder_iterative, [1, 2, 4, 5, 7, 3, 6]),
        (inorder_recursive, inorder_iterative, [4, 2, 7, 5, 1, 3, 6]),
        (postorder_recursive, postorder_iterative, [4, 7, 5, 2, 6, 3, 1]),
        (levelorder_recursive, levelorder_iterative, [[1], [2, 3], [4, 5, 6], [7]]),
    ]:
        assert rec(root) == expected, rec.__name__
        assert it(root) == expected, it.__name__
        assert rec(None) == it(None) == [], rec.__name__
    print("all traversals ok")
