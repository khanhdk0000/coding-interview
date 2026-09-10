def solve(N, A):
    # Each operation skips exactly one index and adds 1 to the other N-1.
    # Let k = total operations, c_i = how many operations skipped index i.
    #   sum(c_i) = k        and        A_i = k - c_i,  c_i >= 0
    # Summing A_i: S = N*k - k = k*(N-1)  =>  k = S / (N-1)
    # Feasible iff (N-1) divides S and every A_i <= k (so c_i >= 0).
    S = sum(A)
    if S % (N - 1):
        return -1
    k = S // (N - 1)
    return k if max(A) <= k else -1


T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    out_ = solve(N, A)
    print(out_)
