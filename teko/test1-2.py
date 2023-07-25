def main():
    fileMap = {}
    numTests = input()
    for i in range(int(numTests)):
        processUnion()

def processUnion():
    lenSeq = input()
    # firstLen, secondLen = int(lenSeq[0]), int(lenSeq[1])
    numArr = []
    firstArrStr = input()
    sencondArrStr = input()
    firstArr = firstArrStr.split(" ")
    secondArr = sencondArrStr.split(" ")
    for i in firstArr:
        numArr.append(int(i))
    for i in secondArr:
        numArr.append(int(i))
    unique_arr = list(set(numArr))
    unique_arr.sort()
    print(" ".join(str(x) for x in unique_arr))