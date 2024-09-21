function lexicalOrder(n: number): number[] {
  // sort the numbers in lexicographical order, must be O(n) time complexity
  const result: number[] = [];
  let current = 1;
  for (let i = 0; i < n; i++) {
    result.push(current);
    if (current * 10 <= n) {
      current *= 10;
    } else if (current % 10 !== 9 && current + 1 <= n) {
      current++;
    } else {
      while (Math.floor(current / 10) % 10 === 9) {
        current = Math.floor(current / 10);
      }
      current = Math.floor(current / 10) + 1;
    }
  }
  return result;
}
