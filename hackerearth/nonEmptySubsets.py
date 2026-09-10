def solve(A):
    """OR only ever sets bits, so a single element beats any bigger subset."""
    return min(A)


t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))

    out_ = solve(A)
    print(out_)
