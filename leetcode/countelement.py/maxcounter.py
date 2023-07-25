def solution(N, A):
    counters = [0] * N
    max_counter = 0
    last_max_counter = 0

    for op in A:
        if 1 <= op <= N:
            counters[op-1] = max(counters[op-1], last_max_counter) + 1
            max_counter = max(max_counter, counters[op-1])
        elif op == N + 1:
            last_max_counter = max_counter

    for i in range(N):
        counters[i] = max(counters[i], last_max_counter)

    return counters