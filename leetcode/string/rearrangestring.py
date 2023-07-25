import heapq
def reorganizeString(s: str) -> str:
    charMap = {}
    for i in s:
        if i not in charMap:
            charMap[i] = 0
        charMap[i] += 1
    appearList = [(-val, key) for key, val in charMap.items()]
    heapq.heapify(appearList)
    res = ""
    prevVal, prevKey = 0, ""

    while appearList:
        val, key = appearList.pop(0)
        if len(res) > 1 and key == res[-1]:
            break

        if prevVal < 0:
            heapq.heappush(appearList, (prevVal, prevKey))
        res += key
        prevVal, prevKey = val + 1, key
    print(res)
    return res if len(res) == len(s) else ""
input = "aaab"
#vlvov
print(reorganizeString(input))

