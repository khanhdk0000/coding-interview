function fishAlive(A: number[], B: number[]): number {
  const n = A.length;
  const stack: number[] = [];
  let fishAlive = 0;

  for (let i = 0; i < n; i++) {
    fishAlive++;
    if (B[i] === 1) {
      stack.push(A[i]);
    } else {
      while (stack.length > 0) {
        fishAlive--;
        const last = stack[stack.length - 1];
        if (last < A[i]) {
          stack.pop();
        } else {
          break;
        }
      }
    }
  }

  return fishAlive;
}
