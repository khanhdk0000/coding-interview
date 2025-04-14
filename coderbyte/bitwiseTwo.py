# /****************************************************************
#  *             CODERBYTE BITWISE TWO CHALLENGE                  *
#  *                                                              *
#  * Problem Statement                                            *
#  * Have the function BitwiseTwo(strArr) take the array of       *
#  * strings stored in strArr, which will only contain two        *
#  * strings of equal length that represent binary numbers, and   *
#  * return a final binary string that performed the              *
#  * bitwise AND operation on both strings. A bitwise AND         *
#  * operation places a 1 in the new string where there is a 1 in *
#  * both locations in the binary strings, otherwise it places    *
#  * a 0 in that spot.                                            *
#  * For example: if strArr is ["10111", "01101"] then your       *
#  * program should return the string "00101"                     *
#  *                                                              *
#  * Examples                                                     *
#  * Input 1: ["100", "000"]                                      *
#  * Output 1: 000                                                *
#  *                                                              *
#  * Input 2: ["10100", "11100"]                                  *
#  * Output 2: 10100                                              *
#  *                                                              *
#  ***************************************************************/

def BitwiseTwo(strArr):
    str1, str2 = strArr
    result = []
    for bit1, bit2 in zip(str1, str2):
        result.append('1' if bit1 == '1' and bit2 == '1' else '0')
    return ''.join(result)

print(BitwiseTwo(["10111", "01101"]))  # Expected output: "00101"
print(BitwiseTwo(["100", "000"]))      # Expected output: "000"
print(BitwiseTwo(["10100", "11100"]))  # Expected output: "10100"