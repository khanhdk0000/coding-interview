def solve(N, A):
    # One operation: A[i] += 2, A[j] -= 1  (i == j allowed -- sample 1 has N=1)
    # so each operation changes the total sum by exactly +1.
    #
    # Let k = number of operations. Final sum must be 0, so S + k = 0 => k = -S.
    # The count is forced by the sum; there is nothing to minimize.
    #
    # Feasibility: let p_i = times i was the "+2" index, q_i = times the "-1" index.
    #   A_i + 2*p_i - q_i = 0  =>  q_i = A_i + 2*p_i,  and  sum(p) = sum(q) = k
    # q_i >= 0 forces p_i >= ceil(-A_i / 2) for every negative A_i.
    # Padding any p_i upward keeps q_i >= 0, so the only real constraint is that
    # the forced minimum of sum(p) fits inside k.
    S = sum(A)
    k = -S
    if k < 0:
        return -1
    need = sum((-a + 1) // 2 for a in A if a < 0)  # ceil(|a| / 2)
    return k if need <= k else -1


T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    out_ = solve(N, A)
    print(out_)
