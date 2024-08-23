// Definition for a binary tree node.
class TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;
  constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }
}

function sumNumbers(root: TreeNode | null): number {
  if (!root) {
    return 0;
  }

  // Dfs
  const stack: {
    node: TreeNode;
    path: string;
  }[] = [];
  const visited = new Set();
  let totalPath: number[] = [];
  stack.push({
    node: root,
    path: `${root.val}`,
  });
  while (stack.length > 0) {
    const { node, path } = stack.pop() as { node: TreeNode; path: string };
    if (!node.left && !node.right) {
      totalPath.push(parseInt(`${path}`));
      continue;
    }
    if (node.left && !visited.has(node.left)) {
      stack.push({
        node: node.left,
        path: `${path}${node.left.val}`,
      });
      visited.add(node.left);
    }
    if (node.right && !visited.has(node.right)) {
      stack.push({
        node: node.right,
        path: `${path}${node.right.val}`,
      });
      visited.add(node.right);
    }
  }
  return totalPath.reduce((acc, cur) => acc + cur, 0);
}
