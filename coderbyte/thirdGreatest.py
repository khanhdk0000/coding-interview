# /****************************************************************
#  *             CODERBYTE THIRD GREATEST CHALLENGE               *
#  *                                                              *
#  * Problem Statement                                            *
#  * Have the function ThirdGreatest(strArr) take the array of    *
#  * strings stored in strArr and return the third largest word   *
#  * within it. So For Example:                                   *
#  * if strArr is ["hello", "world", "before", "all"] your output *
#  * should be world because "before" is 6 letters long,          *
#  * and "hello" and "world" are both 5, but the output should be *
#  * world because it appeared as the last 5 letter word in the   *
#  * array. If strArr was ["hello", "world", "after", "all"] the  *
#  * output should be after because the first three words are all *
#  * 5 letters long, so return the last one. The array will have  *
#  * at least three strings and each string will only contain     *
#  * letters.                                                     *
#  *                                                              *
#  * Examples                                                     *
#  * Input 1: new string[] {"coder","byte","code"}                *
#  * Output 1: code                                               *
#  *                                                              *
#  * Input 2: new string[] {"abc","defg","z","hijk"}              *
#  * Output 2: abc                                                *
#  *                                                              *
#  ***************************************************************/

def ThirdGreatest(strArr):
    # Sort the array by the length of the strings in descending order
    sortedArr = sorted(strArr, key=len, reverse=True)
    
    # Get the third largest word
    thirdLargest = sortedArr[2]
    
    return thirdLargest

def ThirdGreatest(strArr: List[str]) -> str:
    first = second = third = ""
    
    for word in strArr:
        length = len(word)

        if length > len(first) or (length == len(first)):
            third = second
            second = first
            first = word
        elif length > len(second) or (length == len(second)):
            third = second
            second = word
        elif length > len(third) or (length == len(third)):
            third = word

    return third