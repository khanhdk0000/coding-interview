class _Node {
  val: number;
  children: _Node[];
  constructor(val?: number) {
    this.val = val === undefined ? 0 : val;
    this.children = [];
  }
}

function postorder(root: _Node | null): number[] {
  const result: number[] = [];
  function postorder(node: _Node | null) {
    if (node === null) return;
    for (let child of node.children) {
      postorder(child);
    }
    result.push(node.val);
  }
  postorder(root);
  return result;
}
