# /
#               CODERBYTE DISTINCT CHARACTERS CHALLENGE          
                                                               
#   Problem Statement                                            
#   Have the function DistinctCharacters(str) take the str       
#   parameter being passed and determine if it contains at least 
#   10 distinct characters, if so, then your program should      
#   return the string true, otherwise it should return the string
#   false. For example: if str is "abc123kkmmmm?" then your      
#   program should return the string false because this string   
#   contains only                                                
#   9 distinct characters: a, b, c, 1, 2, 3, k, m, ? adds up to 9
                                                               
#   Examples                                                     
#   Input 1: 12334bbmma:=6                                       
#   Output 1: true                                               
                                                               
#   Input 2: eeeemmmmmmmmm1000                                   
#   Output 2: false                                              
#  /

def DistinctCharacters(str):
    # Create a set to store distinct characters
    distinct_chars = set()

    # Iterate through each character in the string
    for char in str:
        # Add the character to the set
        distinct_chars.add(char)

        # If we have 10 or more distinct characters, return true
        if len(distinct_chars) >= 10:
            return "true"

    # If we finish the loop and have less than 10, return false
    return "false"

print(DistinctCharacters("abc123kkmmmm?"))  # Output: false
print(DistinctCharacters("12334bbmma:=6"))  # Output: true
print(DistinctCharacters("eeeemmmmmmmmm1000"))  # Output: false