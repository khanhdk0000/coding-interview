def solve(A, k):
    """Two shapes of move sequence matter: pop k elements and expose A[k], or
    pop k-1 and spend the last move pushing back the best one seen. Leftover
    moves are burned on pop/push cycles, which needs two elements to juggle,
    so a single-element stack is the one case parity can strand."""
    n = len(A)
    if n == 1:
        return A[0] if k % 2 == 0 else -1

    best = -1
    if k >= 2:
        best = max(A[:min(k - 1, n)])
    if k < n:
        best = max(best, A[k])
    return best


n, k = map(int, input().split())
A = list(map(int, input().split()))

out_ = solve(A, k)
print(out_)
