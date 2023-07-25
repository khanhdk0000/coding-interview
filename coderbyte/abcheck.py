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
    count = 0
    idxa = -1
    idxb = -1
    for i in range(len(str)):
        if str[i] == 'a':
            idxa = i
            # print('a', idxa, idxb)
            if idxb != -1 and abs(idxa-idxb) - 1 == 3:
                return True
        elif str[i] == 'b':
            idxb = i
            # print('b', idxa, idxb)
            if idxa != -1 and abs(idxa-idxb) - 1 == 3:
                return True
    return False


input = "after badly"
# input = "Laura sobs"
print(ABCheck(input))