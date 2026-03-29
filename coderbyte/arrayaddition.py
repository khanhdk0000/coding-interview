# /****************************************************************
#  *             CODERBYTE ARRAY ADDITION I CHALLENGE             *
#  *                                                              *
#  * Problem Statement                                            *
#  * Have the function ArrayAdditionI(arr) take the array of      *
#  * numbers stored in arr and return the string true if any      *
#  * combination of numbers in the array (excluding the largest   *
#  * number) can be added up to equal the largest number in the   *
#  * array, otherwise return the string false.                    *
#  * For example: if arr contains [4, 6, 23, 10, 1, 3] the output *
#  * should return true because 4 + 6 + 10 + 3 = 23. The array    *
#  * will not be empty, will not contain all the same elements,   *
#  * and may contain negative numbers.                            *
#  *                                                              *
#  * Examples                                                     *
#  * Input 1: [5,7,16,1,2]                                        *
#  * Output 1: false                                              *
#  *                                                              *
#  * Input 2: [3,5,-1,8,12]                                       *
#  * Output 2: true                                               *
#  *                                                              *
#  ***************************************************************/

def ArrayAdditionI(arr):
    # Find the largest number in the array
    largest = max(arr)
    
    # Remove the largest number from the array
    arr.remove(largest)
    
    # Initialize a set to keep track of possible sums
    possible_sums = {0}
    
    # Iterate through each number in the array
    for num in arr:
        # Create a new set to store new sums
        new_sums = set()
        
        # For each existing sum, add the current number and store it in new_sums
        for s in possible_sums:
            new_sums.add(s + num)
        
        # Update possible_sums with new_sums
        possible_sums.update(new_sums)
    
    # Check if the largest number can be formed by any combination of other numbers
    return "true" if largest in possible_sums else "false"

# Test cases
print(ArrayAdditionI([5, 7, 16, 1, 2]))  # Output: false
print(ArrayAdditionI([3, 5, -1, 8, 12]))  # Output: true
print(ArrayAdditionI([4, 6, 23, 10, 1, 3]))  # Output: true
