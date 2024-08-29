function removeStones(stones: number[][]): number {
  const n = stones.length;
  const uf = new UnionFind(n);
  for (let i = 0; i < n; i++) {
    for (let j = i + 1; j < n; j++) {
      if (stones[i][0] === stones[j][0] || stones[i][1] === stones[j][1]) {
        uf.union(i, j);
      }
    }
  }
  return n - uf.count;
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