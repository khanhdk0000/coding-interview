def solve(N, A, B):
    """Span between the first and last index where A and B differ."""
    lo = 0
    while lo < N and A[lo] == B[lo]:
        lo += 1
    if lo == N:
        return 0
    hi = N - 1
    while A[hi] == B[hi]:
        hi -= 1
    return hi - lo + 1


T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    out_ = solve(N, A, B)
    print(out_)
