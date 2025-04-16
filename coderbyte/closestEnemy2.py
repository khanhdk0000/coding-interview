# // For this challenge you will search in a matrix for an enemy.
# /*
# have the function ClosestEnemyII(strArr) read the matrix of numbers stored in strArr which will be a 2D matrix that contains only the integers 1, 0, or 2. Then from the position in the matrix where a 1 is, return the number of spaces either left, right, down, or up you must move to reach an enemy which is represented by a 2. You are able to wrap around one side of the matrix to the other as well. For example: if strArr is ["0000", "1000", "0002", "0002"] then this looks like the following:

# 0 0 0 0
# 1 0 0 0
# 0 0 0 2
# 0 0 0 2

# For this input your program should return 2 because the closest enemy (2) is 2 spaces away from the 1 by moving left to wrap to the other side and then moving down once. The array will contain any number of 0's and 2's, but only a single 1. It may not contain any 2's at all as well, where in that case your program should return a 0.
# */

def ClosestEnemyII(strArr):
    # Convert the input strings to a 2D list of integers
    matrix = [list(map(int, row)) for row in strArr]

    # Find the position of the 1 in the matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                one_pos = (i, j)
                break

    # Initialize the closest distance to a large number
    closest_distance = float('inf')

    # Iterate through the matrix to find the closest enemy (2)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 2:
                # Calculate the distance considering wrapping
                distance = min(abs(i - one_pos[0]), len(matrix) - abs(i - one_pos[0])) + min(abs(j - one_pos[1]), len(matrix[i]) - abs(j - one_pos[1]))
                closest_distance = min(closest_distance, distance)

    # If no enemy is found, return 0
    return closest_distance if closest_distance != float('inf') else 0

print(ClosestEnemyII(["0000", "1000", "0002", "0002"]))  # Output: 2
print(ClosestEnemyII(["0000", "1000", "0000", "0000"]))  # Output: 0