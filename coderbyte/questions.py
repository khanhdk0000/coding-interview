def QuestionsMarks(strParam):
  foundPair = False
  num = 0
  startCount = False
  count = 0
  for c in strParam:
    if c.isdigit():
      if num == 0:
        num = int(c)
        startCount = True
      else:
        if num + int(c) == 10:
          foundPair = True
        #   startCount = False
          if count != 3:
            return False
          count = 0
        num = int(c)
    elif c == '?' and startCount:
      count += 1

  return foundPair

# keep this function call here
input = "9???1???9???1???9" 
print(QuestionsMarks(input))