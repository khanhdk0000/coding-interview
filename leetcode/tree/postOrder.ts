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

function postorderTraversal(root: TreeNode | null): number[] {
    const result: number[] = [];
    function postorder(node: TreeNode | null) {
        if (node === null) return;
        postorder(node.left);
        postorder(node.right);
        result.push(node.val);
    }
    postorder(root);
    return result;
}

