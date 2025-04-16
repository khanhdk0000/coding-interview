#For this challenge you will be searching for the smallest time difference.
#have the function TimeDifference(strArr) read the array of strings stored in strArr which will be an unsorted list of times in a twelve-hour format like so: HH:MM(am/pm). Your goal is to determine the smallest difference in minutes between two of the times in the list. For example: if strArr is ["2:10pm", "1:30pm", "10:30am", "4:42pm"] then your program should return 40 because the smallest difference is between 1:30pm and 2:10pm with a difference of 40 minutes. The input array will always contain at least two elements and all of the elements will be in the correct format and unique. 

def TimeDifference(strArr):
    def convertTo24Hour(time):
        timeStamp, period = time[:-2], time[-2:]
        hour, minute = map(int, timeStamp.split(':'))
        if period == 'pm' and hour != 12:
            hour += 12
        elif period == 'am' and hour == 12:
            hour = 0
        return hour * 60 + minute
    
    # Convert all times to minutes
    times = [convertTo24Hour(time) for time in strArr]
    times.sort()
    result = float('inf')
    n = len(times)
    # Calculate the differences between consecutive times
    for i in range(1, n):
        diff = times[i] - times[i - 1]
        result = min(result, diff)
    
    return result

print(TimeDifference(["2:10pm", "1:30pm", "10:30am", "4:42pm"]))  # Output: 40
print(TimeDifference(["12:30pm", "12:00am"]))  # Output: 690