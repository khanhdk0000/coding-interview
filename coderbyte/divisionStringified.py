# /***************************************************************************************
# *                                                                                      *
# *                  CODERBYTE BEGINNER CHALLENGE                                        *
# *                                                                                      *
# *  Division Stringified                                                                *
# *  Have the function DivisionStringified(num1,num2)     *
# *  take both parameters being passed, divide num1 by num2, and return the result as    *
# *  a string with properly formatted commas. If an answer is only 3 digits long,        *
# *  return the number with no commas (ie. 2 / 3 should output "1"). For example:        *
# *  if num1 is 123456789 and num2 is 10000 the output should be "12,345".               *
# *                                                                                      *

def DivisionStringified(num1, num2):
    quotient = round(num1 / num2)

    # 2) stringify with commas via the standard format mini‑language
    result = f"{quotient:,}"

    # 3) omit commas for 3‑digit or shorter outputs
    return result if len(result) > 3 else str(quotient)

print(DivisionStringified(123456789, 10000))  # Output: "12,345"