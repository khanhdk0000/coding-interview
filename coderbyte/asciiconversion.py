# /
#               CODERBYTE ASCII CONVERTION CHALLENGE             
                                                               
#   Problem Statement                                            
#   Have the function ASCIIConversion(str) take the str parameter
#   being passed and return a new string where every character,  
#   aside from the space character, is replaced with its         
#   corresponding decimal character code. For example: if str is 
#   "dog" then your program should return the string 100111103   
#   because d = 100, o = 111, g = 103.                           
                                                               
#   Examples                                                     
#   Input 1: "hello world"                                       
#   Output 1: 104101108108111 119111114108100                    
                                                               
#   Input 2: "abc **"                                            
#   Output 2: 979899 4242                                        
#  /

def ASCIIConversion(inputStr):
    # Initialize an empty list to store the ASCII values
    ascii_values = []

    # Iterate through each character in the string
    for char in inputStr:
        # If the character is not a space, convert it to its ASCII value
        if char != ' ':
            ascii_values.append(str(ord(char)))
        else:
            ascii_values.append(' ')  # Keep spaces as they are

    # Join the list into a single string and return it
    return ''.join(ascii_values)

print(ASCIIConversion("hello world"))  # Output: 104101108108111 119111114108100
print(ASCIIConversion("abc **"))  # Output: 979899 4242
print(ASCIIConversion("dog"))  # Output: 100111103