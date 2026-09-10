import sys


def solve(n, IA, IR):
    """a_i = n - IA[i] - IR[n+1-i], then verify IA is genuinely A's inversion table."""
    A = [0] * n
    seen = bytearray(n + 1)
    for i in range(n):
        v = n - IA[i] - IR[n - 1 - i]
        if v < 1 or v > n or seen[v]:
            return None
        seen[v] = 1
        A[i] = v

    # Verify: count values already placed that exceed A[i]. Fenwick over values.
    tree = [0] * (n + 1)
    for i in range(n):
        v = A[i]
        smaller_or_eq = 0          # how many placed values are <= v
        k = v
        while k > 0:
            smaller_or_eq += tree[k]
            k -= k & -k
        if i - smaller_or_eq != IA[i]:
            return None
        k = v
        while k <= n:
            tree[k] += 1
            k += k & -k
    return A


data = sys.stdin.buffer.read().split()
pos = 0
T = int(data[pos]); pos += 1
out = []
for _ in range(T):
    n = int(data[pos]); pos += 1
    IA = list(map(int, data[pos:pos + n])); pos += n
    IR = list(map(int, data[pos:pos + n])); pos += n

    A = solve(n, IA, IR)
    out.append(" ".join(map(str, A)) if A else "-1")
sys.stdout.write("\n".join(out) + "\n")
