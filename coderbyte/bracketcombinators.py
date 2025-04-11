def BracketCombinations(num):
    result = []
    def backtrack(current, open, close):
        if open == 0 and close == 0:
            result.append(current)
            return
        
        if open > 0:
            backtrack(current + '(', open - 1, close)
        
        if close > open:
            backtrack(current + ')', open, close - 1)
    backtrack('', num, num)
    return len(result)


# keep this function call here 
input = 3
print(BracketCombinations(input))

