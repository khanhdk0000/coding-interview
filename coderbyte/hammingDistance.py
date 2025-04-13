# /****************************************************************
#  *             CODERBYTE HAMMING DISTANCE CHALLENGE             *
#  *                                                              *
#  * Problem Statement                                            *
#  * Have the function HammingDistance(strArr) take the array of  *
#  * strings stored in strArr, which will only contain two strings*
#  * of equal length and return the Hamming distance between them.*
#  * The Hamming distance is the number of positions where the    *
#  * corresponding characters are different.                      *
#  * For example: if strArr is ["coder", "codec"] then your       *
#  * program should return 1. The string will always be of equal  *
#  * length and will only contain lowercase characters from the   *
#  * alphabet and numbers.                                        *
#  *                                                              *
#  * Examples                                                     *
#  * Input 1: ["10011", "10100"]                                  *
#  * Output 1: 3                                                  *
#  *                                                              *
#  * Input 2: ["helloworld", "worldhello"]                        *
#  * Output 2: 8                                                  *
#  *                                                              *
#  ***************************************************************/

def HammingDistance(strArr):
    if len(strArr) != 2:
        return "Invalid input"
    str1, str2 = strArr
    if len(str1) != len(str2):
        return "Strings must be of equal length"
    distance = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            distance += 1
    return distance

print(HammingDistance(["10011", "10100"]))  # Output: 3
print(HammingDistance(["helloworld", "worldhello"]))  # Output: 8