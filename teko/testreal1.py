def main():
    n = int(input())
    incidents = []
    inci = input()
    inciLst = inci.split(" ")
    for i in range(n):   
        incidents.append(int(inciLst[i]))
    process(incidents)

def process(incidents):
    numEng = 0
    unhandle = 0
    for i in incidents:
        if i == -1:
            if numEng > 0:
                numEng -= 1
            else:
                unhandle += 1
        else:
            numEng += i
    print(unhandle)
main()