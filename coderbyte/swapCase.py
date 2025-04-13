# *                                                                                      *
# *                  CODERBYTE BEGINNER CHALLENGE                                        *
# *                                                                                      *
# *  Swap Case                                                                           *
# *  Using the JavaScript language, have the function SwapCase(str) take the str         *
# *  parameter and swap the case of each character. For example: if str is "Hello World" *
# *  the output should be hELLO wORLD. Let numbers and symbols stay the way they are.    *   

def SwapCase(str):
    result = ""
    for char in str:
        if char.isalpha():
            if char.islower():
                result += char.upper()
            else:
                result += char.lower()
        else:
            result += char
    return result

print(SwapCase("Hello World"))  # Output: "hELLO wORLD"