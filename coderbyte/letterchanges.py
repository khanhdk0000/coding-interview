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
def encrypt(text,s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            if (char.isupper()):
                result += chr((ord(char) + s-65) % 26 + 65)
            else:
                result += chr((ord(char) + s - 97) % 26 + 97)
        else:
            result += char 
    return result

def letterChanges(strArr):
    strArr = encrypt(strArr, 1)
    res = ""
    for c in strArr:
        if c in ['a', 'e', 'i', 'o', 'u']:
            res += c.upper()
        else:
            res += c
    return res



# keep this function call here 
# input = "hello*3"
input = "fun times!"
print(letterChanges(input))
