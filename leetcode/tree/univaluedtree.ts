/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function isUnivalTree(root: TreeNode | null): boolean {
    return treeTraverseCheck(root.left, root.val) && treeTraverseCheck(root.right, root.val);
};

function treeTraverseCheck(node: TreeNode | null, value: number): boolean {
    if (node === null) {
        return true;
    }
    if (node.val !== value) {
        return false;
    }
    return treeTraverseCheck(node.left, value) && treeTraverseCheck(node.right, value);
}