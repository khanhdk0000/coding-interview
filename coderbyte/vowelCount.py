# /****************************************************************
#  *             CODERBYTE VOWEL COUNT CHALLENGE                  *
#  *                                                              *
#  * Problem Statement                                            *
#  * Have the function VowelCount(str) take the str string        *
#  * parameter being passed and return the number of vowels the   *
#  * string contains (ie. "All cows eat grass and moo" would      *
#  * return 8). Do not count y as a vowel for this challenge.     *
#  *                                                              *
#  * Examples                                                     *
#  * Input 1: "hello"                                             *
#  * Output 1: 2                                                  *
#  *                                                              *
#  * Input 2: "coderbyte"                                         *
#  * Output 2: 3                                                  *
#  *                                                              *
#  * Solution Efficiency                                          *
#  * The user scored higher than 20.7% of users who solved this   *
#  * challenge.                                                   *
#  *                                                              *
#  ***************************************************************/

def VowelCount(str):
    # Define a set of vowels
    vowels = set("aeiouAEIOU")
    
    # Initialize a counter
    count = 0
    
    # Iterate through each character in the string
    for char in str:
        # If the character is a vowel, increment the counter
        if char in vowels:
            count += 1
            
    return count

# keep this function call here
print(VowelCount("hello"))
print(VowelCount("coderbyte"))
print(VowelCount("All cows eat grass and moo"))
