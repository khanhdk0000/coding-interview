# /****************************************************************
#  *             CODERBYTE AB CHECKS CHALLENGE                    *
#  *                                                              *
#  * Problem Statement                                            *
#  * Have the function ABCheck(str) take the str parameter being  *
#  * passed and return the string true if the characters a and b  *
#  * are separated by exactly 3 places anywhere in the string at  *
#  * least once (ie. "lane borrowed" would result in true because *
#  * there is exactly three characters between a and b).          *
#  * Otherwise return the string false.                           *
#  *                                                              *
#  * Examples                                                     *
#  * Input 1: after badly                                         *
#  * Output 1: false                                              *
#  *                                                              *
#  * Input 2: Laura sobs                                          *
#  * Output 2: true                                               *
#  *                                                              *
#  ***************************************************************/
def ABCheck(str):
    indexA = -1
    indexB = -1

    for i in range(len(str)):
        if str[i] == 'a':
            indexA = i
        elif str[i] == 'b':
            indexB = i

        # Check if we have found both 'a' and 'b'
        if indexA != -1 and indexB != -1:
            # Check if they are separated by exactly 3 characters
            if abs(indexA - indexB) == 4:
                return "true"
    
    # If we finish the loop without finding a valid pair, return "false"
    return "false"


input = "after badly"
# input = "Laura sobs"
print(ABCheck(input))
print(ABCheck("Laura sobs"))