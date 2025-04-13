# /****************************************************************
#  *             CODERBYTE COUNTING MINUTES ONE CHALLENGE         *
#  *                                                              *
#  * Problem Statement                                            *
#  * Have the function CountingMinutesI(str) take the str         *
#  * parameter being passed which will be two times               *
#  * (each properly formatted with a colon and am or pm)          *
#  * separated by a hyphen and return the total number of minutes *
#  * between the two times. The time will be in a 12 hour clock   *
#  * format.                                                      * 
#  * For example: if str is 9:00am-10:00am then the               *
#  * output should be 60. If str is 1:00pm-11:00am the output     *
#  * should be 1320.                                              *
#  *                                                              *
#  * Examples                                                     *
#  * Input 1: "12:30pm-12:00am"                                   *
#  * Output 1: 690                                                *
#  *                                                              *
#  * Input 2: "1:23am-1:08am"                                     *
#  * Output 2: 1425                                               *
#  *                                                              *
#  * Solution Efficiency                                          *
#  * The user scored higher than 44.7% of users who solved this   *
#  * challenge.                                                   *
#  *                                                              *
#  ***************************************************************/


def CountingMinutesI(str):
    start, end = str.split('-')
    def convertTo24Hour(time):
        timeStamp, period = time[:-2], time[-2:]
        hour, minute = map(int, timeStamp.split(':'))
        if period == 'pm' and hour != 12:
            hour += 12
        elif period == 'am' and hour == 12:
            hour = 0
        return hour * 60 + minute

    # Convert start and end times to 24-hour format
    startTime = convertTo24Hour(start)
    endTime = convertTo24Hour(end)
    print(f"Start Time: {startTime}, End Time: {endTime}")
    # Calculate the difference in minutes
    if endTime < startTime:
        endTime += 24*60
    return endTime - startTime
print(CountingMinutesI("12:30pm-12:00am"))  # Output: 690
print(CountingMinutesI("1:23am-1:08am"))    # Output: 1425
print(CountingMinutesI("9:00am-10:00am"))  # Output: 60
print(CountingMinutesI("1:00pm-11:00am"))  # Output: 1320