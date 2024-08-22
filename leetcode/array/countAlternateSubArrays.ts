function countAlternatingSubarrays(nums: number[]): number {
  let left = 0;
  let right = 0;
  let count = 0;
  while (right < nums.length - 1) {
    if (nums[right] === nums[right + 1]) {
      const n = right - left + 1;
      count += (n * (n + 1)) / 2;
      left = right + 1;
      right++;
    } else {
      right++;
    }
  }
  if (left < nums.length) {
    const n = right - left + 1;
    count += (n * (n + 1)) / 2;
  }
  return count;
}
