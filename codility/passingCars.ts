function passingCars(A: number[]): number {
  let count = 0;
  let sum = 0;
  for (let i = 0; i < A.length; i++) {
    if (A[i] === 0) {
      count++;
    } else {
      sum += count;
    }
  }
  return sum > 1000000000 ? -1 : sum;
}
