def solve(A, k):
    """The switch to a queue happens once, so a plan is just "pop i from the
    top, then take k - i from the bottom". Both sides are prefix sums, and i
    runs 1..k because at least one element must come off the stack."""
    from_bottom = [0] * (k + 1)
    for j in range(1, k + 1):
        from_bottom[j] = from_bottom[j - 1] + A[-j]

    best = 0
    from_top = 0
    for i in range(1, k + 1):
        from_top += A[i - 1]
        best = max(best, from_top + from_bottom[k - i])
    return best


n, k = map(int, input().split())
A = list(map(int, input().split()))

out_ = solve(A, k)
print(out_)
