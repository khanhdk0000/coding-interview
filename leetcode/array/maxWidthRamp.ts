function maxWidthRamp(nums: number[]): number {
  const stack: number[] = [];
  const n = nums.length;

  // Monotonic stack
  // Build a decreasing stack of indices
  for (let i = 0; i < n; i++) {
    if (stack.length === 0 || nums[i] < nums[stack[stack.length - 1]]) {
      stack.push(i);
    }
  }

  let maxWidth = 0;

  // Traverse from the end to the beginning
  for (let j = n - 1; j >= 0; j--) {
    while (stack.length > 0 && nums[j] >= nums[stack[stack.length - 1]]) {
      const i = stack.pop()!;
      maxWidth = Math.max(maxWidth, j - i);
    }
  }

  return maxWidth;
}
