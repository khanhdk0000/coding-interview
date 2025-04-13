# /****************************************************************
#  *              CODERBYTE BITWISE ONE CHALLENGE                 *
#  *                                                              *
#  * Problem Statement                                            *
#  * Have the function BitwiseOne(strArr) take the array of       *
#  * strings stored in strArr, which will only contain two        *
#  * strings of equal length that represent binary numbers, and   *
#  * return a final binary string that performed the bitwise      *
#  * OR operation on both strings. A bitwise OR operation places  *
#  * a 0 in the new string where there are zeroes in both binary  *
#  * strings, otherwise it places a 1 in that spot.               *
#  * For example: if strArr is ["1001", "0100"] then your program *
#  * should return the string "1101"                              *
#  *                                                              *
#  * Examples                                                     *
#  * Input 1: ["100", "000"]                                      *
#  * Output 1: 100                                                *
#  *                                                              *
#  * Input 2: ["00011", "01010"]                                  *
#  * Output 2: 01011                                              *
#  *                                                              *
#  ***************************************************************/

def BitwiseOne(strArr):
    if len(strArr) != 2:
        return "Invalid input"
    str1, str2 = strArr
    if len(str1) != len(str2):
        return "Strings must be of equal length"
    result = []
    for i in range(len(str1)):
        if str1[i] == '1' or str2[i] == '1':
            result.append('1')
        else:
            result.append('0')
    return ''.join(result)

print(BitwiseOne(["1001", "0100"]))  # Output: 1101
print(BitwiseOne(["100", "000"]))    # Output: 100
print(BitwiseOne(["00011", "01010"]))  # Output: 01011