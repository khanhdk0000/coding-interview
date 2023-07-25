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

# function countingMinutesI(str) {
#     let times = str.split('-');

#     times = times.map(function(currentValue, index, array) {
#         let pairs = currentValue.split(':');
#         let time =
#             (pairs[1][2] === 'a'
#                 ? parseInt(pairs[0]) % 12
#                 : (parseInt(pairs[0]) % 12) + 12) *
#                 60 +
#             parseInt(pairs[1][0] + pairs[1][1]);
#         return time;
#     });

#     let diff = times[1] - times[0];
#     return diff < 0 ? diff + 1440 : diff;
}

def countTime(str):
    div = str.split(':')
    res = 0
    hours = 0
    if div[1][2] == 'a':
        res = int(div[0]) 

def CountingMinutesI(str):
    times = str.split('-')
    time1 = 0

input = "12:30pm-12:00am" 
print(CountingMinutesI(input))