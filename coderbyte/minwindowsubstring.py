def MinWindowSubstring(strArr):
    bigStr, subStr = strArr[0], strArr[1]
    if subStr == "":
        return bigStr
    left, right = 0, 0
    subStrMap = {}
    for i in subStr:
        if i not in subStrMap:
            subStrMap[i] = 0
        subStrMap[i] += 1
    charsAppeared = list(subStrMap.keys())
    while right < len(bigStr) and len(charsAppeared) > 0:
        char = bigStr[right]
        if char in subStrMap:
            subStrMap[char] -= 1
            if subStrMap[char] == 0:
                charsAppeared.remove(char)
        right += 1

    while left < right:
        char = bigStr[left]
        if char in subStrMap: 
            if subStrMap[char] < 0:
                subStrMap[char] += 1
            else:
                break
        left += 1

    return bigStr[left:right]

input = ['ahffaksfajeeubsne', 'jefaa']
# aksfaje
# input = ["aaffhkksemckelloe", "fhea"]
# affhkkse
# input = ["aaffsfsfasfasfasfasfasfacasfafe", "fafe"]
# 
# keep this function call here 
print(MinWindowSubstring(input))