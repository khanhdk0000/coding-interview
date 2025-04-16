                                                               
#   Problem Statement                                            
#   Have the function ClosestEnemy(arr) take the array of numbers
#   stored in arr and from the position in the array where a 1	
#   is, return the number of spaces either left or right you	
#   must move to reach an enemy which is represented by a 2.	
#   For example: if arr is [0, 0, 1, 0, 0, 2, 0, 2] then your	
#   program should return 3 because the closest enemy (2) is 3	
#   spaces away from the 1. The array will contain any number of	
#   0's and 2's, but only a single 1. It may not contain any 2's	
#   at all as well, where in that case your program should	
#   return a 0. 							
                                                               
#   Examples                                                     
#   Input 1: [1, 0, 0, 0, 2, 2, 2] 	                        
#   Output 1: 4                                                  
                                                               
#   Input 2: [2, 0, 0, 0, 2, 2, 1, 0]                            
#   Output 2: 1                                                  
                                                               

def ClosestEnemy(arr):
    # Find the index of the 1 in the array
    one_index = arr.index(1)

    # Initialize the closest distance to a large number
    closest_distance = float('inf')

    # Iterate through the array to find the closest enemy (2)
    for i in range(len(arr)):
        if arr[i] == 2:
            distance = abs(i - one_index)
            if distance < closest_distance:
                closest_distance = distance

    # If no enemy is found, return 0
    return closest_distance if closest_distance != float('inf') else 0
    

print(ClosestEnemy([1, 0, 0, 0, 2, 2, 2]))  # Output: 4
print(ClosestEnemy([2, 0, 0, 0, 2, 2, 1, 0]))  # Output: 1
print(ClosestEnemy([0, 0, 1, 0, 0, 2, 0, 2]))  # Output: 3
print(ClosestEnemy([0, 0, 1, 0, 0, 0]))  # Output: 0