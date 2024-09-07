class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

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

function isSubPath(head: ListNode | null, root: TreeNode | null): boolean {
    // iterative approach
    if (!head) return true;
    if (!root) return false;
    const stack = [[head, root]];
    while (stack.length) {
        const [node, tree] = stack.pop() as [ListNode, TreeNode];
        if (isSub(node, tree)) return true;
        if (tree.left) stack.push([node, tree.left]);
        if (tree.right) stack.push([node, tree.right]);
    }
    return false;
}

function isSub(node: ListNode | null, tree: TreeNode | null): boolean {
    if (!node) return true;
    if (!tree) return false;
    if (node.val !== tree.val) return false;
    return isSub(node.next, tree.left) || isSub(node.next, tree.right);
}
