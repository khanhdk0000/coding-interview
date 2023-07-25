# Tekoer has forgot his secret PIN code. His PIN code contains 4 ditgits (0 to 9) and can start with 0. 
# He remembers only some characteristics of the PIN code, and described them in a string S of length 
# 10. where:
# 	+ Si is o if the PIN contains at least one digit i.
# 	+ Si is x if the PIN doesn't contain any digits.
# 	+ Si ? if he isn't sure the PIN contains digits i or not.
# Write function in python to count the number of all PIN codes that have the characteristics described in the string S.
# 
# Ex: xxoxxxxxxx returns 1
# 	  ooo???xxxx returns 108

import math
def main():
    password = input()
    process(password)
    
def process(S):
    mustAppear = set()
    question = set()
    calMap = {0: 0,  1: 1, 2: 14, 3: 36, 4: 24}

    for idx, val in enumerate(S):
        if val == "o":
            mustAppear.add(idx)
        elif val == "?":
            question.add(idx)
    n = len(mustAppear)
    if n == 4:
        return 24
    numAppear = calMap[n]

    for i in range(1, 4 - n +1):
        digits = n + i
        if i > len(question):
            break
        combination = math.comb(len(question), i)
        numAppear += calMap[digits] * combination
    print(numAppear)
# main()
# input = "ooo???xxxx"
input = "xxoxxxxxxx"
process(input)