def solve(A, queries):
    """Bucket each value's total contribution by its frequency, then prefix-sum
    over frequencies so every query is one subtraction."""
    freq = {}
    for value in A:
        freq[value] = freq.get(value, 0) + 1

    sum_by_freq = [0] * (len(A) + 1)
    for value, f in freq.items():
        sum_by_freq[f] += value * f
    print(sum_by_freq)

    prefix = [0] * len(sum_by_freq)
    running = 0
    for f, total in enumerate(sum_by_freq):
        running += total
        prefix[f] = running
    print(prefix)

    return [prefix[r] - prefix[l - 1] for l, r in queries]


n = int(input())
A = list(map(int, input().split()))
q = int(input())
queries = [tuple(map(int, input().split())) for _ in range(q)]

out_ = solve(A, queries)
print("\n".join(map(str, out_)))
