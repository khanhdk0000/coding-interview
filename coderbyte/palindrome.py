# /****************************************************************
#  *             CODERBYTE PALINDROME TWO CHALLENGE               *
#  *                                                              *
#  * Problem Statement                                            *
#  * Have the function PalindromeTwo(str) take the str parameter  * 
#  * being passed and return the string true if the parameter is  *
#  * a palindrome, (the string is the same forward as it is       *
#  * backward) otherwise return the string false. The parameter   *
#  * entered may have punctuation and symbols but they should not *
#  * affect whether the string is in fact a palindrome.           *
#  * For example: "Anne, I vote more cars race Rome-to-Vienna"    *
#  * should return true.                                          *
#  *                                                              *
#  * Examples                                                     *
#  * Input 1: "Noel - sees Leon"                                  *
#  * Output 1: true                                               *
#  *                                                              *
#  * Input 2: "A war at Tarawa!"                                  *
#  * Output 2: true                                               *
#  *                                                              *
#  * Solution Efficiency                                          *
#  * The user scored higher than 33.1% of users who solved this   *
#  * challenge.                                                   *
#  *                                                              *
#  ***************************************************************/

def PalindromeTwo(str):
    
    # Remove all non-alphanumeric characters and convert to lowercase
    cleaned_str = ''.join(char.lower() for char in str if char.isalnum())
    
    # Check if the cleaned string is equal to its reverse
    return cleaned_str == cleaned_str[::-1]

input = "Anne, I vote more cars race Rome-to-Vienna"
print(PalindromeTwo(input))
print(PalindromeTwo("Noel - sees Leon"))
print(PalindromeTwo("A war at Tarawa!"))