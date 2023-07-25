def main():
    n = int(input())
    snow = []
    snowStr = input()
    snowStrList = snowStr.split(" ")
    for i in range(n):   
        snow.append(int(snowStrList[i]))
    process(snow)

def process(snow):
    # snowSet = list(set(snow))
    # print(len(snowSet))
    # print(len(snowSet) // 3)
    count = 0
    res = 0
    snowSet = {}
    for i in snow:

        if i not in snowSet:
            snowSet[i] = 0
            count += 1

        if count == 3:
            res += 1
            count = 0
            snowSet = {}
    print(res)

    # return True
main()