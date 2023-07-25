s = "CODEBANC"
t = "ABC"
left = 0
right = 

for i in range(left + 1, right):
    if s[i] in t:
        left = i
        right = left + winLen - 1
        continue