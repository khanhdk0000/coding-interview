from typing import List

def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    actualCost, countingCost, startStation = 0, 0, 0

    for i in range(len(gas)):
        actualCost += gas[i] - cost[i]
        countingCost += gas[i] - cost[i]
        if countingCost < 0:
            countingCost = 0
            startStation = i + 1
    return -1 if actualCost < 0 else startStation