import heapq

# Time:  O(Q log Q) -- each put pushes one heap entry, each entry popped at most once.
# Space: O(Q)       -- val/freq hold <= N keys, heap holds <= Q entries (stale ones included).


def solve(N, Q, operations):
    res = []
    val = {}
    freq = {}
    heap = []          # (freq, key), lazy deletion

    for t, k, v in operations:
        if t == 1:
            res.append(val.get(k, -1))
            continue

        if k in val:                      # update: freq bumps
            val[k] = v
            freq[k] += 1
            heapq.heappush(heap, (freq[k], k))
        else:
            if len(val) >= N:             # evict min freq, smallest key on tie
                while True:
                    f, ek = heapq.heappop(heap)
                    if ek in val and freq[ek] == f:
                        del val[ek]
                        del freq[ek]
                        break
            val[k] = v
            freq[k] = 1
            heapq.heappush(heap, (1, k))

    return res


if __name__ == '__main__':
    ops = [(1, 2, -1), (2, 1, 3), (2, 2, 4), (2, 4, 5), (1, 2, -1)]
    got = solve(2, 5, ops)
    # assert got == [-1, 4], got
    print(' '.join(map(str, got)))
