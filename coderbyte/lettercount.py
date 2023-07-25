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
    words = str.split()
    bestCount = 0
    res = ""
    for w in words:
        maxWordCount = 0
        wordMap = {}
        for c in w:
            if c not in wordMap:
                wordMap[c] = 0
            wordMap[c] += 1

            if wordMap[c] > 1 and wordMap[c] > maxWordCount:
                maxWordCount = wordMap[c]
        if maxWordCount > bestCount:
            bestCount= maxWordCount
            res = w

    return res if res != "" else -1

input = "No words"
print(LetterCountI(input))