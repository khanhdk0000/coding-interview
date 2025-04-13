# /************************************************************************
#  *                 CODERBYTE WAVE SORTING CHALLENGE                     *
#  *                                                                      *
#  * Problem Statement                                                    *
#  * Have the function WaveSorting(arr) take the array of positive integer*
#  * stored in arr and return the string true if the numbers can be       *
#  * arranged in a wave pattern: a1 > a2 < a3 > a4 < a5 > ..., otherwise  *
#  * return the string false. For example, if arr is: [0, 1, 2, 4, 1, 4], *
#  * then a possible wave ordering of the numbers is: [2, 0, 4, 1, 4, 1]. *
#  * So for this input your program should return the string true.        *
#  * The input array will always contain at least 2 elements.             *
#  * More examples are given below as sample test cases.                  *
#  *                                                                      *
#  * Examples                                                             *
#  * Input 1: [0, 1, 2, 4, 1, 1, 1]                                       *
#  * Output 1: false                                                      *
#  *                                                                      *
#  * Input 2: [0, 4, 22, 4, 14, 4, 2]                                     *
#  * Output 2: true                                                       *
#  *                                                                      *
#  ***********************************************************************/

def WaveSorting(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    maxFreq = max(freq.values())
    if maxFreq >= (len(arr) + 1) // 2:
        return "false"
    return "true"

print(WaveSorting([0, 1, 2, 4, 1, 1, 1]))  # Output: false
print(WaveSorting([0, 4, 22, 4, 14, 4, 2]))  # Output: true
print(WaveSorting([1, 2, 3, 4, 5]))  # Output: true