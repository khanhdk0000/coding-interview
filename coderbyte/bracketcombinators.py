def BracketCombinations(num):
    b = 1
    # calculating n!
    for i in range(1, num + 1, 1):
        b = b * i
    # calculating n! * n!
    b = b * b
    d = 1
    # calculating (2n)!
    for i in range(1, 2 * num + 1, 1):
        d = d * i
    # calculating (2n)! / (n! * n!)
    ans = d / b
    # calculating (2n)! / ((n! * n!) * (n+1))
    ans = ans / (num + 1)
    return ans

# keep this function call here 
input = 3
print(BracketCombinations(input))