function maxNumEdgesToRemove(n: number, edges: number[][]): number {
  let res = 0;
  let alice = new UnionFind(n);
  let bob = new UnionFind(n);
  for (const [type, u, v] of edges) {
    if (type === 3) {
      if (!alice.union(u, v)) {
        res++;
      } else {
        bob.union(u, v);
      }
    }
  }
  for (const [type, u, v] of edges) {
    if (type === 1) {
      if (!alice.union(u, v)) {
        res++;
      }
    } else if (type === 2) {
      if (!bob.union(u, v)) {
        res++;
      }
    }
  }
  return alice.count === 1 && bob.count === 1 ? res : -1;
}

class UnionFind {
  parent: number[];
  count: number;
  constructor(n: number) {
    this.parent = Array.from({ length: n }, (_, i) => i);
    this.count = n;
    console.log(this.parent);
  }
  find(x: number): number {
    if (x !== this.parent[x]) {
      this.parent[x] = this.find(this.parent[x]);
    }
    return this.parent[x];
  }
  union(x: number, y: number): boolean {
    const rootX = this.find(x);
    const rootY = this.find(y);
    if (rootX === rootY) {
      return false;
    }
    this.parent[rootX] = rootY;
    this.count--;
    return true;
  }
}
