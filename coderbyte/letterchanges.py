# /****************************************************************
#  *             CODERBYTE LETTER CHANGES CHALLENGE               *
#  *                                                              *
#  * Problem Statement                                            *
#  * Have the function LetterChanges(str) take the str parameter  *
#  * being passed and modify it using the following algorithm.    *
#  * Replace every letter in the string with the letter following *
#  * it in the alphabet (ie. c becomes d, z becomes a). Then      *
#  * capitalize every vowel in this new string (a, e, i, o, u)    *
#  * & finally return this modified string.                       *
#  *                                                              *
#  * Examples                                                     *
#  * Input 1: hello*3                                             *
#  * Ouput 1: Ifmmp*3                                             *
#  *                                                              *
#  * Input 2: fun times!                                          *
#  * Output 2: gvO Ujnft!                                         *
#  *                                                              *
#  * Solution Efficiency                                          *
#  * The user scored higher than 60.4% of users who solved this   *
#  * challenge.                                                   *
#  *                                                              *
#  ***************************************************************/

def letterChanges(strArr):
    result = []
    for c in strArr:
        if c.isalpha():
            letter = c.lower()
            if letter == 'z':
                letter = 'a'
            else:
                letter = chr(ord(letter) + 1)
            if letter in 'aeiou':
                letter = letter.upper()
            elif letter not in 'aeiou' and c.isupper():
                letter = letter.upper()
            result.append(letter)
        else:
            result.append(c)
    return ''.join(result)


# keep this function call here 
# input = "hello*3"
input = "fun times!"
print(letterChanges(input))
print(letterChanges('hello*3'))
