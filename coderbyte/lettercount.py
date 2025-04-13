# /****************************************************************
#  *             CODERBYTE LETTER COUNT ONE CHALLENGE             *
#  *                                                              *
#  * Problem Statement                                            *
#  * Have the function LetterCountI(str) take the str parameter   *
#  * being passed and return the first word with the greatest     *
#  * number of repeated letters.                                  *
#  * For example: "Today, is the greatest day ever!"              *
#  * should return greatest because it has 2 e's (and 2 t's) & it *
#  * comes before ever which also has 2 e's. If there are no      *
#  * words with repeating letters return -1. Words will be        *
#  * separated by spaces.                                         *
#  *                                                              *
#  * Examples                                                     *
#  * Input 1: Hello apple pie                                     *
#  * Output 1: Hello                                              *
#  *                                                              *
#  * Input 2: No words                                            *
#  * Output 2: -1                                                 *
#  *                                                              *
#  * Solution Efficiency                                          *
#  * The user scored higher than 39.2% of users who solved this   *
#  * challenge.                                                   *
#  *                                                              *
#  ***************************************************************/

def LetterCountI(str):
    words = str.split(' ')
    maxCount = 0
    result = '-1'

    for word in words:
        count = {}
        for c in word:
            if c.isalpha():
                count[c] = count.get(c, 0) + 1
        maxChar = max(count.values(), default=0)
        if maxChar > maxCount:
            maxCount = maxChar
            result = word
    return result

input = "No words"
print(LetterCountI(input))
print(LetterCountI("Hello apple pie"))
print(LetterCountI("Today, is the greatest day ever!"))