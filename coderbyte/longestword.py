def LongestWord(sen):

  words = sen.split(' ')
  result = ''
  count = 0
  for word in words:
    localCount = 0
    for c in word:
      if c.isalnum():
        localCount += 1
    if localCount > count:
      count = localCount
      result = word  
  return result

# keep this function call here 
input = "fun&!! time"
print(LongestWord(input))