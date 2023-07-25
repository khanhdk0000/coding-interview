def main():
    numTests = input()
    process()

def process():
    line = "1 2 3 4 6 1"
    lineSplit = line.split(" ") 
    numMap = {}
    numbers = []
    # print(numbers)
    for num in lineSplit:
        # print(num)
        tmp = int(num)
        if num not in numMap:
            numMap[tmp] = -1
        numbers.append(tmp)
    sorted_arr = sorted(numbers)
    # sorted_arr = list(set(sorted_arr))

    for idx, val in enumerate(sorted_arr):
        if numMap[val] == -1:
            numMap[val] = idx

    res = []
    for i in numbers:
        res.append(numMap[i])

    print(" ".join(str(x) for x in res))
process()