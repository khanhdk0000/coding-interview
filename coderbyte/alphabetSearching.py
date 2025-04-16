# /
#               CODERBYTE ALPHABET SEARCHING CHALLENGE           
#                                                                
#   Problem Statement                                            
#   Have the function AlphabetSearching(str) take the string     
#   parameter being passed and return the string true if every   
#   single letter of the English alphabet exists in the string,  
#   otherwise return the string false.                           
#   For example: if str is "zacxyjbbkfgtbhdaielqrm45pnsowtuv"    
#   then your program should return the string true because every
#   character in the alphabet exists in this string even though  
#   some characters appear more than once.                       
#                                                                
#   Examples                                                     
#   Input 1: abcdefghijklmnopqrstuvwxyyyy                        
#   Output 1: false                                              
#                                                                
#   Input 2: abc123456kmo                                        
#   Output 2: false                                              
#  /

def AlphabetSearching(str):
    # Create a set of all letters in the English alphabet
    alphabet_set = set("abcdefghijklmnopqrstuvwxyz")

    # Create a set from the input string
    input_set = set(str.lower())

    for c in alphabet_set:
        if c not in input_set:
            return "false"
    return "true"

print(AlphabetSearching("zacxyjbbkfgtbhdaielqrm45pnsowtuv"))  # true
print(AlphabetSearching("abc123456kmo"))  # false