import sys

MOD = 998244353


def solve(N, M, A, B, Q, queries):
    """F(A,B) = WA*SB + SA*WB, where W is the index-weighted sum."""
    SA = sum(A)
    WA = sum(i * a for i, a in enumerate(A, 1))
    SB = sum(B)
    WB = sum(j * b for j, b in enumerate(B, 1))

    res = [(WA * SB + SA * WB) % MOD]
    for tp, i, j in queries:
        if tp == 1:                       # A[i] <-> B[j]
            x, y = A[i - 1], B[j - 1]
            d = y - x
            SA += d
            WA += i * d
            SB -= d
            WB -= j * d
            A[i - 1], B[j - 1] = y, x
        elif tp == 2:                     # A[i] <-> A[j]
            x, y = A[i - 1], A[j - 1]
            WA += (i - j) * (y - x)
            A[i - 1], A[j - 1] = y, x
        else:                             # B[i] <-> B[j]
            x, y = B[i - 1], B[j - 1]
            WB += (i - j) * (y - x)
            B[i - 1], B[j - 1] = y, x
        res.append((WA * SB + SA * WB) % MOD)
    return res


# ponytail: token cursor, not input() -- up to 5M tokens / 1M query lines here
data = sys.stdin.buffer.read().split()
pos = 0
T = int(data[pos]); pos += 1
out = []
for _ in range(T):
    N = int(data[pos]); pos += 1
    M = int(data[pos]); pos += 1
    A = list(map(int, data[pos:pos + N])); pos += N
    B = list(map(int, data[pos:pos + M])); pos += M
    Q = int(data[pos]); pos += 1
    queries = []
    for _ in range(Q):
        queries.append((int(data[pos]), int(data[pos + 1]), int(data[pos + 2])))
        pos += 3

    out.append(" ".join(map(str, solve(N, M, A, B, Q, queries))))
sys.stdout.write("\n".join(out) + "\n")
