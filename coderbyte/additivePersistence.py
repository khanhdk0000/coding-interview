# /****************************************************************
#  *            CODERBYTE ADDITIVE PERSISTENCE CHALLENGE          *
#  *                                                              *
#  * Problem Statement                                            *
#  * Have the function AdditivePersistence(num) take the num      *
#  * parameter being passed which will always be a positive       *
#  * integer and return its additive persistence which is the     *
#  * number of times you must add the digits in num until you     *
#  * reach a single digit. For example: if num is 2718 then your  *
#  * program should return 2                                      *
#  * because 2 + 7 + 1 + 8 = 18 and 1 + 8 = 9 and you stop at 9.  *
#  *                                                              *
#  * Examples                                                     *
#  * Input 1: 4                                                   *
#  * Output 1: 0                                                  *
#  *                                                              *
#  * Input 2: 19                                                  *
#  * Output 2: 2                                                  *
#  *                                                              *
#  ***************************************************************/

def AdditivePersistence(num):
    result = 0
    while len(str(num)) > 1:
        num = sum(int(i) for i in str(num))
        result += 1
    return result

print(AdditivePersistence(4))  # Output: 0
print(AdditivePersistence(19))  # Output: 2
print(AdditivePersistence(2718))  # Output: 2