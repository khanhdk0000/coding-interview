# For this challenge you will determine if three elements can sum to some larger number.
# have the function ThreeSum(arr) take the array of integers stored in arr, and determine if any three distinct numbers (excluding the first element) in the array can sum up to the first element in the array. For example: if arr is [8, 2, 1, 4, 10, 5, -1, -1] then there are actually three sets of triplets that sum to the number 8: [2, 1, 5], [4, 5, -1] and [10, -1, -1]. Your program should return the string true if 3 distinct elements sum to the first element, otherwise your program should return the string false. The input array will always contain at least 4 elements. 


def ThreeSum(arr):
    def twoSum(nums, target):
        numMap = {}
        res = []
        for i in range(len(nums)):
            if target - nums[i] in numMap:
                res.append([nums[numMap[target - nums[i]]], nums[i]])
            numMap[nums[i]] = i
        return res
    
    target = arr[0]
    nums = arr[1:]
    nums.sort()
    res = []

    # Use two sum to solve three sum
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        twoSumRes = twoSum(nums[i+1:], target - nums[i])
        for pair in twoSumRes:
            res.append([nums[i]] + pair)
    
    return True if len(res) > 0 else False

print(ThreeSum([8, 2, 1, 4, 10, 5, -1, -1]))  # Output: True
print(ThreeSum([8, 2, 1, 4, 10, 5]))  # Output: True
print(ThreeSum([8, 2, 1, 4, 10]))  # Output: False