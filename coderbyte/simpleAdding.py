# /***************************************************************************************
# *                                                                                      *
# *                  CODERBYTE BEGINNER CHALLENGE                                        *
# *                                                                                      *
# *  Simple Adding                                                                       *
# *  Have the function SimpleAdding(num) add up all the                                  *
# *  numbers from 1 to num. For the test cases, the parameter num will be any number     *
# *  from 1 to 1000.                                                                     *
# *                                                                                      *
# *  SOLUTION                                                                            *
# *  This is a simple iterative function that add each number in sequence.               *
# *                                                                                      *
# *  Steps for solution                                                                  *
# *    1) Set var tot to 0.                                                              *
# *    2) Loop from 1 to num and add i by tot to get new tot.                            *
# *    3) Return tot for answer.                                                         *
# *                                                                                      *
# ***************************************************************************************/

def simpleAdding(num):
    # set var tot to 0
    tot = 0

    # loop from 1 to num
    for i in range(1, num + 1):
        # add i by tot to get new tot
        tot += i

    # return tot for answer
    return tot