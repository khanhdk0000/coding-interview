FULL = (1 << 25) - 1


def solve(A):
    """Bit b survives f(i,j) only if every position outside [i,j] has bit b set.
    So [i,j] must cover every zero of that bit: i <= first zero, j >= last zero.
    Prefix/suffix ANDs find those two positions, each bit dropping only once."""
    n = len(A)
    first_zero = [0] * 25
    last_zero = [0] * 25

    run = FULL
    for pos, a in enumerate(A, 1):
        dropped = run & ~a
        run &= a
        while dropped:
            b = (dropped & -dropped).bit_length() - 1
            first_zero[b] = pos
            dropped ^= 1 << b
    total_and = run

    run = FULL
    for pos in range(n, 0, -1):
        dropped = run & ~A[pos - 1]
        run &= A[pos - 1]
        while dropped:
            b = (dropped & -dropped).bit_length() - 1
            last_zero[b] = pos
            dropped ^= 1 << b

    all_pairs = n * (n + 1) // 2
    result = 0
    for b in range(25):
        if total_and >> b & 1:
            pairs = all_pairs  # bit never zero, so every (i,j) keeps it
        else:
            pairs = first_zero[b] * (n - last_zero[b] + 1)
        result += (pairs - 1) << b  # the -1 drops f(1,N), which is always FULL
    return result


t = int(input())
out_ = []
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    out_.append(solve(A))

print("\n".join(map(str, out_)))
