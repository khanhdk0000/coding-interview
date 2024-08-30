function sortColors(nums: number[]): void {
  const numCount = {
    0: 0,
    1: 0,
    2: 0,
  };
  for (let i = 0; i < nums.length; i++) {
    numCount[nums[i]]++;
  }
  for (let i = 0; i < nums.length; i++) {
    if (numCount[0] > 0) {
      nums[i] = 0;
      numCount[0]--;
    } else if (numCount[1] > 0) {
      nums[i] = 1;
      numCount[1]--;
    } else {
      nums[i] = 2;
    }
  }
}
