# /****************************************************************
#  *          CODERBYTE SECOND GREATEST LOWEST CHALLENGE          *
#  *                                                              *
#  * Problem Statement                                            *
#  * Have the function SecondGreatLow(arr) take the array of      *
#  * numbers stored in arr and return the second lowest and second*
#  * greatest numbers, respectively, separated by a space.        *
#  * For example: if arr contains [7, 7, 12, 98, 106] the output  *
#  * should be 12 98. The array will not be empty and will contain*
#  * at least 2 numbers. It can get tricky if there's just        *
#  * two numbers!                                                 *
#  *                                                              *
#  * Examples                                                     *
#  * Input 1: new int[] {1, 42, 42, 180}                          *
#  * Output 1: 42 42                                              *
#  *                                                              *
#  * Input 2: new int[] {4, 90}                                   *
#  * Output 2: 90 4                                               *
#  *                                                              *
#  ***************************************************************/

def SecondGreatLow(arr):
    uniqueSort = sorted(set(arr))
    if len(uniqueSort) == 1:
        return f"{uniqueSort[0]} {uniqueSort[0]}"
    return f"{uniqueSort[1]} {uniqueSort[-2]}"
# Test cases
print(SecondGreatLow([1, 42, 42, 180]))  # Output: "42 42"
print(SecondGreatLow([4, 90]))           # Output: "90 4"
print(SecondGreatLow([7, 7, 12, 98, 106]))  # Output: "12 98"