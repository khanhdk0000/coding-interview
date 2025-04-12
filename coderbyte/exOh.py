# /****************************************************************
#  *             CODERBYTE EX OH CHALLENGE                        *
#  *                                                              *
#  * Problem Statement                                            *
#  * Have the function ExOh(str) take the str parameter being     *
#  * passed & return the string true if there is an equal number  *
#  * of x's & o's, otherwise return the string false. Only these  *
#  * two letters will be entered in the string, no punctuation or *
#  * numbers. For example: if str is "xooxxxxooxo" then the       *
#  * output should return false because there are 6 x's and 5 o's *
#  *                                                              *
#  * Examples                                                     *
#  * Input 1: xooxxo                                              *
#  * Output 1: true                                               *
#  *                                                              *
#  * Input 2: x                                                   *
#  * Output 2: false                                              *
#  *                                                              *
#  * Solution Efficiency                                          *
#  * The user scored higher than 16.8% of users who solved this   *
#  * challenge.                                                   *
#  *                                                              *
#  ***************************************************************/

def ExOh(str):
    count = 0
    for char in str:
        if char == 'x':
            count += 1
        elif char == 'o':
            count -= 1
    return count == 0

# keep this function call here
print(ExOh("xooxxo"))
print(ExOh("x"))
print(ExOh("xooxxxxooxo"))