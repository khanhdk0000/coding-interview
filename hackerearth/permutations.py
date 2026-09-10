import sys


def solve(n, a, queries):
    """Outside [l,r] is prefix [1,l-1] plus suffix [r+1,n]; take the larger max."""
    pre = [0] * (n + 2)          # pre[i] = max of a[1..i]
    for i in range(1, n + 1):
        pre[i] = pre[i - 1] if pre[i - 1] > a[i - 1] else a[i - 1]

    suf = [0] * (n + 2)          # suf[i] = max of a[i..n]
    for i in range(n, 0, -1):
        suf[i] = suf[i + 1] if suf[i + 1] > a[i - 1] else a[i - 1]

    out = []
    for l, r in queries:
        left, right = pre[l - 1], suf[r + 1]
        out.append(left if left > right else right)
    return out


n, q = map(int, input().split())
a = list(map(int, input().split()))
queries = []
for _ in range(q):
    l, r = map(int, input().split())
    queries.append((l, r))

for out_ in solve(n, a, queries):
    print(out_)

# Faster variant if the above TLEs (1e5 query lines -> 1e5 input() calls):
#
# data = sys.stdin.buffer.read().split()
# n = int(data[0])
# q = int(data[1])
# a = list(map(int, data[2:2 + n]))
# pos = 2 + n
# queries = [(int(data[pos + 2 * k]), int(data[pos + 2 * k + 1])) for k in range(q)]
#
# sys.stdout.write("\n".join(map(str, solve(n, a, queries))) + "\n")
