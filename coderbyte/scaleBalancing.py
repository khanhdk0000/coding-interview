# /
#               CODERBYTE SCALE BALANCING CHALLENGE              
#                                                                
#   Problem Statement                                            
#   Have the function ScaleBalancing(strArr) read strArr which   
#   will contain two elements, the first being the two positive  
#   integer weights on a balance scale (left and right sides)    
#   and the second element being a list of available weights as  
#   positive integers. Your goal is to determine if you can      
#   balance the scale by using the least amount of weights from  
#   the list, but using at most only 2 weights.                  
                                                               
#   For example: if strArr is ["[5, 9]", "[1, 2, 6, 7]"] then    
#   this means there is a balance scale with a weight of 5 on    
#   the left side and 9 on the right side. It is in fact         
#   possible to balance this scale by adding a 6 to the left     
#   side from the list of weights and adding a 2 to the right    
#   side. Both scales will now equal 11 and they are perfectly   
#   balanced.                                                    
                                                               
#   Your program should return a comma separated string of the   
#   weights that were used from the list in ascending order,     
#   so for this example your code should return the string 2,6   
                                                               
#   There will only ever be one unique solution and the list of  
#   available weights will not be empty. It is also possible to  
#   add two weights to only one side of the scale to balance it. 
#   If it is not possible to balance the scale then your program 
#   should return the string not possible.                       
                                                               
#   Examples                                                     
#   Input 1: ["[3, 4]", "[1, 2, 7, 7]"]                          
#   Output 1: 1                                                  
                                                               
#   Input 2: ["[13, 4]", "[1, 2, 3, 6, 14]"]                     
#   Output 2: 3,6                                                
#                                                                
#  /

def ScaleBalancing(strArr):
    # Parse the input
    left, right = map(int, strArr[0][1:-1].split(","))
    weights = list(map(int, strArr[1][1:-1].split(",")))

    if left <= right:
        light, heavy = left, right
    else:
        light, heavy = right, left
    diff = heavy - light

    if diff in weights:
        return str(diff)
    
    for i in range(len(weights)):
        for j in range(i + 1, len(weights)):
            w1, w2 = weights[i], weights[j]
            if w1 + w2 == diff:
                return f"{min(w1, w2)},{max(w1, w2)}"
            elif abs(w1 - w2) == diff:
                return f"{min(w1, w2)},{max(w1, w2)}"

    return "not possible"

print(ScaleBalancing(["[5, 9]", "[1, 2, 6, 7]"]))  # Output: "2,6"
print(ScaleBalancing(["[3, 4]", "[1, 2, 7, 7]"]))  # Output: "1"
print(ScaleBalancing(["[13, 4]", "[1, 2, 3, 6, 14]"]))  # Output: "3,6"