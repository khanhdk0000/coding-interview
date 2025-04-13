# /****************************************************************
#  *             CODERBYTE MEAN MODE CHALLENGE                    *
#  *                                                              *
#  * Problem Statement                                            *
#  * Have the function MeanMode(arr) take the array of numbers    *
#  * stored in arr and return 1 if the mode equals the mean, 0 if *
#  * they don't equal each other (ie. [5, 3, 3, 3, 1] should      *
#  * return 1 because the mode (3) equals the mean (3)).          *
#  *                                                              *
#  * The array will not be empty, will only contain positive      *
#  * integers, and will not contain more than one mode.           *
#  *                                                              *
#  * Examples                                                     *
#  * Input 1: new int[] {1, 2, 3}                                 *
#  * Output 1: 0                                                  *
#  *                                                              *
#  * Input 2: new int[] {4, 4, 4, 6, 2}                           *
#  * Output 2: 1                                                  *
#  *                                                              *
#  ***************************************************************/

def MeanMode(arr):
    # Calculate the mean
    mean = sum(arr) / len(arr)
    
    # Count the occurrences of each number
    count = {}
    for num in arr:
        count[num] = count.get(num, 0) + 1
    
    # Find the mode (the number with the highest frequency)
    mode = max(count, key=count.get)
    
    # Check if the mode equals the mean
    return 1 if mode == mean else 0

# Test cases
print(MeanMode([1, 2, 3]))          # Output: 0
print(MeanMode([4, 4, 4, 6, 2]))    # Output: 1