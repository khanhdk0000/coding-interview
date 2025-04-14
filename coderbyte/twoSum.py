# For this challenge you will determine if two elements can sum to some larger number.
# have the function TwoSum(arr) take the array of integers stored in arr, and determine if any two numbers (excluding the first element) in the array can sum up to the first element in the array. For example: if arr is [7, 3, 5, 2, -4, 8, 11], then there are actually two pairs that sum to the number 7: [5, 2] and [-4, 11]. Your program should return all pairs, with the numbers separated by a comma, in the order the first number appears in the array. Pairs should be separated by a space. So for the example above, your program would return: 5,2 -4,11 

def TwoSum(arr):
    target = arr[0]
    pairs = []
    seen = {}
    for num in arr[1:]:
        remain = target - num
        if remain in seen:
            pairs.append(f"{remain},{num}")
        seen[num] = True
    return " ".join(pairs) if pairs else -1

print(TwoSum([7, 3, 5, 2, -4, 8, 11])) # Expected output: "5,2 -4,11"
print(TwoSum([5, 2, 3, 1, 4])) # Expected output: "2,3 1,4"
print(TwoSum([1, 2, 3, 4, 5])) # Expected output: -1    
