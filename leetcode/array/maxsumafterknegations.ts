function largestSumAfterKNegations(nums: number[], k: number): number {
    nums.sort((a, b) => a - b);
    let i = 0;
    while (k > 0 && i < nums.length) {
        if (nums[i] < 0) {
            nums[i] = -nums[i];
            k--;
            i++;
        } else {
            break;
        }
    }
    if (k % 2 === 1) {
        let min = Math.min(...nums);
        let minIndex = nums.indexOf(min);
        nums[minIndex] = -nums[minIndex];
    }
    return nums.reduce((acc, cur) => acc + cur, 0);
};

// Time complexity: O(nlogn)
// Space complexity: O(1)