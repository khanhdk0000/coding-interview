# /****************************************************************
#  *             CODERBYTE OFF LINE MINIMUM CHALLENGE             *
#  *                                                              *
#  * Problem Statement                                            *
#  * Have the function OffLineMinimum(strArr) take the strArr     *
#  * parameter being passed which will be an array of integers    *
#  * ranging from 1...n and the letter "E" and return the correct *
#  * subset based on the following rules. The input will be in    *
#  * the following format: ["I","I","E","I",...,"E",...,"I"] where*
#  * the I's stand for integers and the E means take out the      *
#  * smallest integer currently in the whole set. When finished,  *
#  * your program should return that new set with integers        *
#  * separated by commas. For example: if strArr is               *
#  * ["5","4","6","E","1","7","E","E","3","2"] then your program  *
#  * should return 4,1,5.                                         *
#  *                                                              *
#  * Examples                                                     *
#  * Input 1: ["1","2","E","E","3"]                               *
#  * Output 1: 1,2                                                *
#  *                                                              *
#  * Input 2: ["4","E","1","E","2","E","3","E"]                   *
#  * Output 2: 4,1,2,3                                            *
#  *                                                              *
#  * Solution Efficiency                                          *
#  * The user scored higher than 34.8% of users who solved this   *
#  * challenge.                                                   *
#  ***************************************************************/

import heapq
def OffLineMinimum(strArr):
    minHeap = []
    result = []
    for num in strArr:
        if num == "E":
            if minHeap:
                result.append(str(heapq.heappop(minHeap)))
        else:
            heapq.heappush(minHeap, int(num))
    return ','.join(result)

print(OffLineMinimum(["5","4","6","E","1","7","E","E","3","2"]))  # Output: 4,1,5
print(OffLineMinimum(["1","2","E","E","3"]))  # Output: 1,2
print(OffLineMinimum(["4","E","1","E","2","E","3","E"]))  # Output: 4,1,2,3