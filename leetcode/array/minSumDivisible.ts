function minSubarray(nums: number[], p: number): number {
    const n = nums.length;
    const totalSum = nums.reduce((acc, num) => (acc + num) % p, 0);
    if (totalSum === 0) return 0;
  
    const modMap = new Map<number, number>();
    modMap.set(0, -1); // Initialize with sum 0 at index -1
  
    let result = n;
    let prefixMod = 0;
  
    for (let i = 0; i < n; i++) {
      prefixMod = (prefixMod + nums[i]) % p;
      const neededMod = (prefixMod - totalSum + p) % p;
  
      if (modMap.has(neededMod)) {
        result = Math.min(result, i - modMap.get(neededMod)!);
      }
  
      // Update the map with the current prefixMod
      modMap.set(prefixMod, i);
    }
  
    return result < n ? result : -1;
  }
  