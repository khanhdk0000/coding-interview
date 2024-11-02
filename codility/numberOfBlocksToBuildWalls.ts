function numberOfBlocksToBuildWalls(H: number[]): number {
  const n = H.length;
  const stack: number[] = [];
  let blocks = 0;

  for (let i = 0; i < n; i++) {
    while (stack.length > 0 && stack[stack.length - 1] > H[i]) {
      stack.pop();
    }

    if (stack.length === 0 || stack[stack.length - 1] < H[i]) {
      stack.push(H[i]);
      blocks++;
    }
  }

  return blocks;
}
