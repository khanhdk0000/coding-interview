# *  Powers of Two                                                                       *
# *  the function PowersofTwo(num) take the num      *
# *  parameter being passed which will be an integer and return the string true if       *
# *  it's a power of two. If it's not return the string false. For example if the        *
# *  input is 16 then your program should return the string true but if the input is     *
# *  22 then the output should be the string false                                       *

def PowersofTwo(num):
    # Check if the number is less than or equal to 0
    if num <= 0:
        return "false"
    
    # Check if the number is a power of two
    while num > 1:
        if num % 2 != 0:
            return "false"
        num //= 2
    
    return "true" if num == 1 else "false"

print(PowersofTwo(16))  # Output: "true"
print(PowersofTwo(22))  # Output: "false"