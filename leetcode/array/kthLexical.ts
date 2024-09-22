function findKthNumber(n: number, k: number): number {
    let current = 1;
    k -= 1; // Adjust k because we start from 1
  
    while (k > 0) {
      const steps = calculateSteps(n, current, current + 1);
      if (steps <= k) {
        // Move to the next prefix
        current += 1;
        k -= steps;
      } else {
        // Move to the next level
        current *= 10;
        k -= 1;
      }
    }
  
    return current;
  }
  
  function calculateSteps(n: number, first: number, last: number): number {
    let steps = 0;
    while (first <= n) {
      steps += Math.min(n + 1, last) - first;
      first *= 10;
      last *= 10;
    }
    return steps;
  }
  