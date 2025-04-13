# /****************************************************************
#  *          CODERBYTE NON REPEATING CHARACTERS CHALLENGE        *
#  *                                                              *
#  * Problem Statement                                            *
#  * Have the function NonrepeatingCharacter(str) take the str    *
#  * parameter being passed, which will contain only alphabetic   *
#  * characters and spaces, and return the first non-repeating    *
#  * character. For example: if str is "agettkgaeee" then your    *
#  * program should return k. The string will always contain at   *
#  * least one character and there will always be at least one    *
#  * non-repeating character.                                     *
#  *                                                              *
#  * Examples                                                     *
#  * Input 1: "abcdef"                                            *
#  * Output 1: a                                                  *
#  *                                                              *
#  * Input 2: "hello world hi hey"                                *
#  * Output 2: w                                                  *
#  *                                                              *
#  ***************************************************************/

def NonrepeatingCharacter(str):
    freq = {}
    for c in str:
        freq[c] = freq.get(c, 0) + 1
    for c in str:
        if freq[c] == 1:
            return c
    return ''

print(NonrepeatingCharacter('agettkgaeee')) # Output: k
print(NonrepeatingCharacter('abcdef')) # Output: a
print(NonrepeatingCharacter('hello world hi hey')) # Output: w