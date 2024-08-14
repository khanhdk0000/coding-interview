function smallestDistancePair(nums: number[], k: number): number {
    // Step 1: Sort the array to make pair distance calculation manageable
    nums.sort((a, b) => a - b);
    
    // Step 2: Set the bounds for binary search based on possible distances
    let low = 0;
    let high = nums[nums.length - 1] - nums[0];

    // Helper function to count pairs with distance <= mid
    function countPairs(mid: number): number {
        let count = 0;
        let start = 0;
        
        for (let end = 1; end < nums.length; end++) {
            while (nums[end] - nums[start] > mid) {
                start++;
            }
            count += end - start;
        }
        
        return count;
    }

    // Step 3: Binary search to find the k-th smallest distance
    while (low < high) {
        let mid = Math.floor((low + high) / 2);
        if (countPairs(mid) < k) {
            low = mid + 1;
        } else {
            high = mid;
        }
    }

    // Since low and high converge to the smallest distance where countPairs(distance) >= k
    return low;
}
