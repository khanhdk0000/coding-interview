# *  Number Addition                                                                     *
# *  The function NumberSearch(str) take the str     *
# *  parameter, search for all the numbers in the string, add them together, then        *
# *  return that final number. For example: if str is "88Hello 3World!" the output       *
# *  should be 91. You will have to differentiate between single digit numbers and       *
# *  multiple digit numbers like in the example above. So "55Hello" and "5Hello 5"       *
# *  should return two different answers. Each string will contain at least one letter   *
# *  or symbol.                                                                          *

def NumberAddition(str):
    total = 0
    currentNumber = ""

    for c in str:
        if c.isdigit():
            currentNumber += c
        else:
            if currentNumber:
                total += int(currentNumber)
                currentNumber = ""

    if currentNumber:
        total += int(currentNumber)
    return total

print(NumberAddition("88Hello 3World!"))  # Output: 91
print(NumberAddition("55Hello"))          # Output: 55
print(NumberAddition("5Hello 5"))        # Output: 10