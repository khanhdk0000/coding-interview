# /****************************************************************
#  *             CODERBYTE OVERLAPPING RANGES CHALLENGE           *
#  *                                                              *
#  * Problem Statement                                            *
#  * Have the function OverlappingRanges(arr) take the array of   *
#  * numbers stored in arr which will contain 5 positive integers,*
#  * the first two representing a range of numbers (a to b), the  *
#  * next 2 also representing another range of integers (c to d), *
#  * and a final 5th element (x) which will also be a positive    *
#  * integer, and return the string true if both sets of ranges   *
#  * overlap by at least x numbers.                               *
#  * For example: if arr is [4, 10, 2, 6, 3] then your program    *
#  * should return the string true.                               *
#  * The first range of numbers are 4, 5, 6, 7, 8, 9, 10 & the    *
#  * second range of numbers are 2, 3, 4, 5, 6.                   *
#  * The last element in the array is 3, and there are 3 numbers  *
#  * that overlap between both ranges: 4, 5, and 6.               *
#  * If both ranges do not overlap by at least x numbers,         *
#  * then your program should return the string false.            *
#  *                                                              *
#  * Examples                                                     *
#  * Input 1: [5,11,1,5,1]                                        *
#  * Output 1: true                                               *
#  *                                                              *
#  * Input 2: [1,8,2,4,4]                                         *
#  * Output 2: false                                              *
#  *                                                              *
#  ***************************************************************/

def OverlappingRanges(arr):
    a, b, c, d, x = arr
    # Calculate the overlapping range
    overlapStart = max(a, c)
    overlapEnd = min(b, d)
    # Calculate the number of overlapping integers
    overlapCount = max(0, overlapEnd - overlapStart + 1)
    # Check if the overlap count is at least x
    if overlapCount >= x:
        return "true"
    else:
        return "false"

print(OverlappingRanges([4, 10, 2, 6, 3]))  # Output: "true"
print(OverlappingRanges([5, 11, 1, 5, 1]))  # Output: "true"
print(OverlappingRanges([1, 8, 2, 4, 4]))  # Output: "false"