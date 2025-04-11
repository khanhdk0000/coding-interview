def BracketMatcher(strParam)-> int:
    stack = []
    for char in strParam:
        if char == '(':
            stack.append('(')
        elif char == ')':
            if not stack:
                return 0
            stack.pop()
    return 1 if not stack else 0

print(BracketMatcher("((hello (world))"))  
print(BracketMatcher("(c(oder)) b(yte)"))  