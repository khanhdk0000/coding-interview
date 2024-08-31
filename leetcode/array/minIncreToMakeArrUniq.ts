function minIncrementForUnique(nums: number[]): number {
    nums.sort((a, b) => a - b); // Sort the numbers
    let count = 0;
    let prev = nums[0];

    for (let i = 1; i < nums.length; i++) {
        if (nums[i] <= prev) {
            count += (prev + 1 - nums[i]); // Increment current number to be one more than the previous
            nums[i] = prev + 1; // Update the current number
        }
        prev = nums[i]; // Update prev to the current number
    }

    return count;
}
