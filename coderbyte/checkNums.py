# /***************************************************************************************
# *                                                                                      *
# *                  CODERBYTE BEGINNER CHALLENGE                                        *
# *                                                                                      *
# *  First Factorial                                                                     *
# *  Have the function CheckNums(num1,num2) take both     *
# *  parameters being passed and return the string true if num2 is greater than num1,    *
# *  otherwise return the string false. If the parameter values are equal to each other  *
# *  then return the string -1                                                           *
# *                                                                                      *
# *  SOLUTION                                                                            *
# *  This solution has to use an If...else if...else  statement since you will be        *
# *  comparing for three different comparisons.
# *                                                                                      *
# *  Steps for solution                                                                  *
# *    1) If num1 and num2 are equal then return string -1                               *
# *    2) Else If num2 is greater than num1 then return true                             *
# *    3) Else return false                                                              *
# *                                                                                      *
# ***************************************************************************************/

def CheckNums(num1, num2):
    # check if num1 and num2 are equal
    if num1 == num2:
        return "-1"
    # check if num2 is greater than num1
    elif num2 > num1:
        return "true"
    # else return false
    else:
        return "false"