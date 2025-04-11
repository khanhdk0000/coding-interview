def MinWindowSubstring(strArr):
    charMap = {}
    for c in strArr[1]:
        charMap[c] = charMap.get(c, 0) + 1
    left = 0
    right = 0
    res = ""
    minLen = float('inf')
    count = len(strArr[1])
    while right < len(strArr[0]):
        c = strArr[0][right]
        if c in charMap:
            charMap[c] -= 1
            if charMap[c] >= 0:
                count -= 1
        while count == 0:
            if right - left + 1 < minLen:
                minLen = right - left + 1
                res = strArr[0][left:right+1]
            c = strArr[0][left]
            # Return the character to the map if it is in the map
            if c in charMap:
                charMap[c] += 1
                if charMap[c] > 0:
                    count += 1
            left += 1
        right += 1
    return res





input = ['ahffaksfajeeubsne', 'jefaa']
# aksfaje
# input = ["aaffhkksemckelloe", "fhea"]
# affhkkse
# input = ["aaffsfsfasfasfasfasfasfacasfafe", "fafe"]
# 
# keep this function call here 
print(MinWindowSubstring(input))