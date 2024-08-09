function maximumBags(
  capacity: number[],
  rocks: number[],
  additionalRocks: number
): number {
  const currentCapacity = capacity.map((c, i) => c - rocks[i]);
  // Count number of bags with current = 0
  let count = 0;
  for (let i = 0; i < currentCapacity.length; i++) {
    if (currentCapacity[i] === 0) {
      count++;
    }
  }
  const sortedCapacityAsc = currentCapacity
    .sort((a, b) => a - b)
    .filter((c) => c > 0);
  let currentRock = additionalRocks;
  for (let i = 0; i < sortedCapacityAsc.length; i++) {
    if (currentRock >= sortedCapacityAsc[i]) {
      count++;
      currentRock -= sortedCapacityAsc[i];
    }
  }
  return count;
}
