# /****************************************************************
#  *             CODERBYTE TIME CONVERT CHALLENGE                 *
#  *                                                              *
#  * Problem Statement                                            *
#  * Have the function TimeConvert(num) take the num parameter    *
#  * being passed and return the number of hours and minutes the  *
#  * parameter converts to (ie. if num = 63 then the output       *
#  * should be 1:3). Separate the number of hours and minutes     *
#  * with a colon.                                                *
#  *                                                              *
#  * Examples                                                     *
#  * Input 1: 126                                                 *
#  * Output 1: 2:6                                                *
#  *                                                              *
#  * Input 2: 45                                                  *
#  * Output 2: 0:45                                               *
#  *                                                              *
#  * Solution Efficiency                                          *
#  * The user scored higher than 29.1% of users who solved this   * 
#  * challenge.                                                   *
#  ***************************************************************/

def TimeConvert(num):
    hour = num // 60
    minute = num % 60
    return str(hour) + ":" + str(minute)
# keep this function call here
print(TimeConvert(126))
print(TimeConvert(45))
print(TimeConvert(63))