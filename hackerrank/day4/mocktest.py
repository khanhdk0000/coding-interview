def truckTour(petrolpumps):
    # Write your code here
    n = len(petrolpumps)
    def reachEndPump(startIdx):
        gas = 0
        copyStartIdx = startIdx
        while(startIdx < n):
            gas += petrolpumps[startIdx][0]
            if petrolpumps[startIdx][0] > gas:
                return False
            gas -= petrolpumps[startIdx][1]
            startIdx += 1
        if copyStartIdx > 0:
            idx = 0
            while (idx < copyStartIdx):
                gas += petrolpumps[idx][0]
                if petrolpumps[startIdx][0] > gas:
                    return False
                gas -= petrolpumps[idx][1]
                idx += 1
        return True
    for i in range(len(petrolpumps)):
        if petrolpumps[i][0] < petrolpumps[i][1]:
            continue
        if reachEndPump(i):
            return i
    return -1