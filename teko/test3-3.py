def main():
    line = input()
    lineSplit = line.split(" ")
    numBranch, capacity = int(lineSplit[0]), int(lineSplit[1])
    process(numBranch, capacity)
    process2(numBranch, capacity)

def process(numBranch, capacity):
    tank = 0
    branchLeft = numBranch - 1
    money = 0
    i = 1
    while branchLeft > 0:
        # fill gas
        addGas = capacity - tank
        tank += addGas
        if addGas > branchLeft:
            addGas = branchLeft
        money += i * addGas
        branchLeft -= addGas
        i += 1
        tank -= 1
    print(money)
    # 5 + 2 + 3 + 4 + 5

def process2(numBranch, capacity):
    numBranch -= 1
    if numBranch <= capacity:
        print(int(numBranch))
        return
    
    addGas = numBranch - capacity
    station = addGas + 1
    money = capacity + station*(station+1)/2 - 1
    print(int(money))

main()