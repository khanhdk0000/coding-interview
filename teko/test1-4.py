# def process():
   
#     sorted_indices = sorted(range(len(arrival)), key=lambda i: arrival[i])
    
#     for i in sorted_indices:
#         while busyServers and busyServers[0][0] <= arrival[i]:
#             _, server = busyServers.pop(0)
#             freeServers.append(server)
#         # if not freeServers:
#         #     continue
#         resServer = min(freeServers)
#         if resServer not in resMap:
#             resMap[resServer] = 0
#         busyServers.append((arrival[i] + used[i], resServer))
#     print(len(resMap))
    # return res
import heapq
def process(n, arrival, burstTime):
    # Write your code here
    freeServers = list(range(1, n+1))
    busyServers = []
    res = [-1] * len(arrival)
    resMap = {}
    
    sorted_indices = sorted(range(len(arrival)), key=lambda i: arrival[i])
    
    for i in sorted_indices:
        while busyServers and busyServers[0][0] <= arrival[i]:
            finishedTime, server = heapq.heappop(busyServers)
            heapq.heappush(freeServers, server)
        if not freeServers:
            continue
        resServer = heapq.heappop(freeServers)
        if resServer not in resMap:
            resMap[resServer] = 0
        # res[i] = resServer
        heapq.heappush(busyServers, (arrival[i] + burstTime[i], resServer))
    # return res
    print(len(resMap.keys()))

def main():
    numServer = int(input())
    freeServers = list(range(1, numServer+1))
    arrivalStr = input()
    arrivalStrSpilt = arrivalStr.split(" ")
    arrival = []
    for i in len(numServer):
        arrival.append(int(arrivalStrSpilt[i]))
    # arrival = [int(i) for i in arrivalStrSpilt]
    usedStr = input()
    usedStrSpilt = usedStr.split(" ")
    used = [int(i) for i in usedStrSpilt]

    process(numServer, arrival, used)
main()