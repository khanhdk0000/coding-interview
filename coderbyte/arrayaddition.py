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
#  *                                                              *
#  ***************************************************************/


def ArrayAdditionI(arr):
    # Sort the array in descending order
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    # Get the largest number in the array
    max_num = arr[0]
    # Get the sum of all numbers except the largest one
    sum_except_max = sum(arr[1:])
    # If the sum of all numbers except the largest one is equal to the largest number,
    # return True
    if sum_except_max == max_num:
        return True
    # Otherwise, check if any combination of numbers in the array (excluding the largest
    # number) can be added up to equal the largest number
    for i in range(2, len(arr)):
        for j in range(len(arr)-i+1):
            combo = arr[j:j+i]
            if sum(combo) == max_num:
                return True
    # If no combination of numbers can be added up to equal the largest number, return False
    return False

# input = [5,7,16,1,2]
input = [4, 6, 23, 10, 1, 3]
print(ArrayAdditionI(input))