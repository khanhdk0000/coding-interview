# /
#                CODERBYTE SIMPLE EVENS CHALLENGE                
                                                               
#   Problem Statement                                            
#   Have the function SimpleEvens(num) check whether every single
#   number in the passed in parameter is even. If so, return the  
#   string true, otherwise return the string false. For example: 
#   if num is 4602225 your program should return the string      
#   false because 5 is not an even number.                       
                                                               
#   Examples                                                     
#   Input 1: 2222220222 		                                
#   Output 1: true                                               
                                                               
#   Input 2: 20864646452                                         
#   Output 2: false                                              
                                                               
#  /

def SimpleEvens(num):
    # Convert the number to a string to iterate through each digit
    num_str = str(num)
    
    # Check if every digit is even
    for digit in num_str:
        if int(digit) % 2 != 0:  # If the digit is odd
            return "false"
    
    return "true"

print(SimpleEvens(2222220222))  # Output: true
print(SimpleEvens(20864646452))  # Output: false
print(SimpleEvens(4602225))  # Output: false