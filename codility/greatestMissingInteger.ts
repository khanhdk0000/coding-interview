function greatestMissingInteger(A: number[]): number {
  const positiveSet = new Set<number>();

  for (const num of A) {
    if (num > 0) {
      positiveSet.add(num);
    }
  }

  let smallestMissing = 1;
  while (positiveSet.has(smallestMissing)) {
    smallestMissing++;
  }

  return smallestMissing;
}
