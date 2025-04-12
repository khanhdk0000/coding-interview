def QuestionsMarks(strParam):
  currentQuestionCount = 0
  currentNum = 0
  foundPair = False
  startCount = False
  for c in strParam:
    if c.isdigit():
      if currentNum == 0:
        currentNum = int(c)
        startCount = True
      else:
        if currentNum + int(c) == 10:
          if currentQuestionCount != 3:
            return "false"
          currentQuestionCount = 0
          foundPair = True
        currentNum = int(c)
    elif c == '?' and startCount:
      currentQuestionCount += 1
  return 'true' if foundPair else 'false'

# keep this function call here
input = "arrb6???4xxbl5???eee5"
print(QuestionsMarks(input))