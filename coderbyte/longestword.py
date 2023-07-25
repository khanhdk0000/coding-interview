def LongestWord(sen):

  # code goes here
	res = ""
	count = 0
	maxCount = 0
	left, right = 0, 0
	for i in range(len(sen)):
		if sen[i].isalpha():
			if count == 0:
				count += 1
				left = i
				right = i
			else:
				count += 1
				right += 1
		else:
			if count > maxCount:
				res = sen[left:right+1]
				maxCount = count
			count = 0
	if count > maxCount:
		res = sen[left:right+1]
		maxCount = count
	# print(maxCount)
	return res

# keep this function call here 
input = "fun&!! time"
print(LongestWord(input))