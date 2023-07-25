def FindIntersection(strArr):

  # code goes here
  firstArr = [int(x) for x in strArr[0].split(",")]
  secondArr = [int(x) for x in strArr[1].split(",")]

  lenFirst = len(firstArr)
  lenSecond = len(secondArr)
  idx1, idx2 = 0, 0
  res = []
  while idx1 < lenFirst and idx2 < lenSecond:
    if firstArr[idx1] == secondArr[idx2]:
      res.append(firstArr[idx1])
      idx1 += 1
      idx2 += 1
    elif firstArr[idx1] < secondArr[idx2]:
      idx1 += 1
    elif firstArr[idx1] > secondArr[idx2]:
      idx2 += 1

  return ','.join(str(i) for i in res) if len(res) > 0 else "false"

# keep this function call here 
input = ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
print(FindIntersection(input))

# "9???1???9???1???9"
# 5??aaaaaaaaaaaaaaaaaaa?5?a??5"