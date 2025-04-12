# /****************************************************************
#  *             CODERBYTE LETTER CAPITALIZE CHALLENGE            *
#  *                                                              *
#  * Problem Statement                                            *
#  * Have the function LetterCapitalize(str) take the str         *
#  * parameter being passed and capitalize the first letter of    *
#  * each word. Words will be separated by only one space.        *
#  *                                                              *
#  * Examples                                                     *
#  * Input 1: "hello world"                                       *
#  * Output 1: Hello World                                        *
#  *                                                              *
#  * Input 2: "i ran there"                                       *
#  * Output 2: I Ran There                                        *
#  *                                                              *
#  * Solution Efficiency                                          *
#  * The user scored higher than 50.6% of users who solved this   * 
#  * challenge.                                                   *
#  *                                                              *
#  ***************************************************************/

def LetterCapitalize(str):
    words = str.split(' ')
    result = []

    for word in words:
        if len(word) > 0:
            word = word[0].upper() + word[1:]
        result.append(word)
    return ' '.join(result)
    
# keep this function call here
print(LetterCapitalize("hello world"))
print(LetterCapitalize("i ran there"))