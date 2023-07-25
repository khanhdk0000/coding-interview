# /****************************************************************
#  *             CODERBYTE SIMPLE SYMBOLS CHALLENGE               *
#  *                                                              *
#  * Problem Statement                                            *
#  * Have the function SimpleSymbols(str) take the str parameter  *
#  * being passed and determine if it is an acceptable sequence   *
#  * by either returning the string true or false. The str        *
#  * parameter will be composed of + and = symbols with several   *
#  * characters between them (ie. ++d+===+c++==a) and for the     *
#  * string to be true each letter must be surrounded by          *
#  * a + symbol. So the string to the left would be false.        *
#  * The string will not be empty & will have at least one letter *
#  *                                                              *
#  * Examples                                                     *
#  * Input 1: "+d+=3=+s+"                                         *
#  * Output 1: true                                               *
#  *                                                              *
#  * Input 2: "f++d+"                                             *
#  * Output 2: false                                              *
#  *                                                              *
#  * Solution Efficiency                                          *
#  * The user scored higher than 48.0% of users who solved this   *
#  * challenge.                                                   *
#  ***************************************************************/
def solution(input):
    for i in range(len(input)):
        if input[i].isalpha():
            if i == 0 or input[i - 1] != '+':
                return False
            elif i == len(input) -1 or input[i + 1] != '+':
                return False
    return True


# keep this function call here 
# input = "hello*3"
# input = "+d+=3=+s+"
input = "+f++d"
print(solution(input))