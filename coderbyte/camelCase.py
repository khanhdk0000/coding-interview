# /
#               CODERBYTE CAMEL CASE CHALLENGE                   
                                                               
#   Problem Statement                                            
#   Have the function CamelCase(str) take the str parameter being
#   passed and return it in proper camel case format where the   
#   first letter of each word is capitalized (excluding the first
#   letter). The string will only contain letters and some       
#   combination of delimiter punctuation characters separating   
#   each word.                                                   
                                                               
#   For example: if str is "BOB loves-coding" then your program  
#    should return the string bobLovesCoding.                    
                                                               
#   Examples                                                     
#   Input 1: "cats ANDDogs-are Awesome"                         
#   Output 1: catsAndDogsAreAwesome                              
                                                               
#   Input 2: "a b c d-e-f%g"                                     
#   Output 2: aBCDEFG                                            
#  /

# def CamelCase(str):
#     arr = []
#     currentWord = ''
#     for c in str:
#         if c.isalpha():
#             currentWord += c.lower()
#         else:
#             if currentWord:
#                 arr.append(currentWord)
#                 currentWord = ''
    
#     if currentWord:
#         arr.append(currentWord)

#     # Capitalize the first letter of each word except the first one
#     for i in range(1, len(arr)):
#         arr[i] = arr[i].capitalize()

#     return ''.join(arr)
import re

def CamelCase(s):
    # Split the string into words using non-letter characters as separators
    words = re.split(r'[^a-zA-Z]+', s)

    # Filter out any empty strings in case of multiple delimiters
    words = [word for word in words if word]

    # Return camelCase format
    if not words:
        return ""

    first = words[0].lower()
    rest  = [word.capitalize() for word in words[1:]]
    
    return first + ''.join(rest)

print(CamelCase("cats ANDDogs-are Awesome"))  # Output: catsAndDogsAreAwesome
print(CamelCase("a b c d-e-f%g"))  # Output: aBCDEFG
print(CamelCase("BOB loves-coding"))  # Output: bobLovesCoding