# /****************************************************************
#  *             CODERBYTE DASH INSERT CHALLENGE                  *
#  *                                                              *
#  * Problem Statement                                            *
#  * Have the function DashInsert(str) insert dashes ('-')        *
#  * between each two odd numbers in str. For example: if str is  *
#  * 454793 the output should be 4547-9-3. Don't count zero as an *
#  * odd number.                                                  *
#  *                                                              *
#  * Examples                                                     *
#  * Input 1: 99946                                               *
#  * Output 1: 9-9-946                                            *
#  *                                                              *
#  * Input 2: 56730                                               *
#  * Output 2: 567-30                                             *
#  ***************************************************************/

def DashInsert(str):
    result = ""

    for i in range(len(str)):
        result += str[i]
        if i < len(str) - 1:
            # Check if both current and next characters are odd
            if int(str[i]) % 2 == 1 and int(str[i + 1]) % 2 == 1:
                result += "-"
    return result

# Test cases
print(DashInsert("99946"))  # Output: "9-9-946"
print(DashInsert("56730"))  # Output: "567-30"