import heapq
def getServerIndex(n, arrival, burstTime):
    # Write your code here
    freeServers = list(range(1, n+1))
    busyServers = []
    res = [-1] * len(arrival)
    
    sorted_indices = sorted(range(len(arrival)), key=lambda i: arrival[i])
    
    for i in sorted_indices:
        while busyServers and busyServers[0][0] <= arrival[i]:
            finishedTime, server = heapq.heappop(busyServers)
            heapq.heappush(freeServers, server)
        if not freeServers:
            continue
        resServer = heapq.heappop(freeServers)
        res[i] = resServer
        heapq.heappush(busyServers, (arrival[i] + burstTime[i], resServer))
    return res

n = 4
arrival = [3, 5, 1, 6, 8]
burstTime = [9, 2, 10, 4, 5]

print(getServerIndex(n, arrival, burstTime))