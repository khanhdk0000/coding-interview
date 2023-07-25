import math

def main():
    line = input().split(" ")
    numBag = int(line[0])
    children = int(line[1])
    T = int(line[2])
    bagStr = input()
    bags = [int(i) for i in bagStr.split(" ")]
    print(calculate_minimum_time(numBag, children, T, bags))
    # print(calculate_minimum_time(0, , T, bags))

def calculate_minimum_time(N, C, T, P):
    # Calculate the upper bound on the time required
    total_candies = sum(P)
    max_time = math.ceil(total_candies / (T))

    # Binary search for the minimum time required
    lo = 0
    hi = max_time
    while lo < hi:
        mid = (lo + hi) // 2
        candies_distributed = 0
        for p in P:
            candies_distributed += min(mid // T, p)
            if candies_distributed >= C:
                break
        if candies_distributed >= C:
            hi = mid
        else:
            lo = mid + 1

    return lo

# main()
C = 3
T = 4
bags = [5,8,3,10,7]
print(calculate_minimum_time(0, C, T, bags))