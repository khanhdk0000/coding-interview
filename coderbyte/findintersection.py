def FindIntersection(strArr):
  arrayA = [int(x.strip()) for x in strArr[0].split(",")]
  arrayB = [int(x.strip()) for x in strArr[1].split(",")]

  i, j = 0, 0
  intersection = []
  while i < len(arrayA) and j < len(arrayB):
    if arrayA[i] == arrayB[j]:
      intersection.append(str(arrayA[i]))
      i += 1
      j += 1
    elif arrayA[i] < arrayB[j]:
      i += 1
    else:
      j += 1
  if intersection:
    return ','.join(intersection)
  else:
    return "false"


# keep this function call here 
input = ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
print(FindIntersection(input))
