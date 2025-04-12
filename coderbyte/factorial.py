def FirstFactorial(num):
    # Check if the number is less than 0
    if num < 0:
        return "Undefined for negative numbers"
    
    # Check if the number is 0 or 1
    elif num == 0 or num == 1:
        return 1
    
    # Calculate factorial for numbers greater than 1
    else:
        result = 1
        for i in range(2, num + 1):
            result *= i
        return result