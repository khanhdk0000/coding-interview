from heapq import heappush, heappop


def solve(A):
    """Sweep j left to right and let it claim every earlier index still waiting:
    those with a bigger digit sum and a smaller value. The first j to claim an
    index is the smallest one, so each index is answered once and removed.
    Digit sums stop at 81, so waiting indexes sit in one min-heap per digit sum."""
    digit_sums = [sum(map(int, str(value))) for value in A]
    top = max(digit_sums)
    waiting = [[] for _ in range(top + 1)]
    ans = [-1] * len(A)

    for j, value in enumerate(A):
        for d in range(digit_sums[j] + 1, top + 1):
            bucket = waiting[d]
            while bucket and bucket[0][0] < value:
                ans[heappop(bucket)[1]] = j + 1
        heappush(waiting[digit_sums[j]], (value, j))

    return ans


n, q = map(int, input().split())
A = list(map(int, input().split()))
ans = solve(A)

out_ = [ans[int(input()) - 1] for _ in range(q)]
print("\n".join(map(str, out_)))
