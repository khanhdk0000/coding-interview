function numberOfDivisibleInteger(A: number, B: number, K: number): number {
  // Count of integers divisible by K from 0 up to B
  const countUpToB = Math.floor(B / K);
    
  // Count of integers divisible by K from 0 up to A - 1
  const countUpToA = Math.floor((A - 1) / K);
  
  // Difference gives the count of integers divisible by K in range [A..B]
  return countUpToB - countUpToA;
}
