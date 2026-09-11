import struct
import sys

CELL = 32  # bits reserved per cell; values are < 2^30 so an OR never carries
MASK = (1 << CELL) - 1


def solve(n, m, packed_rows, queries):
    """Each row is packed into one big int, CELL bits per cell, so ORing two
    packed rows ORs all m cells at once. A sparse table over rows answers the
    vertical range in O(1), then a doubling fold collapses the column range."""
    st = [packed_rows]
    k = 1
    while (1 << k) <= n:
        prev = st[-1]
        half = 1 << (k - 1)
        st.append([prev[i] | prev[i + half] for i in range(n - (1 << k) + 1)])
        k += 1

    col_mask = [(1 << (CELL * w)) - 1 for w in range(m + 1)]

    out = []
    for x1, y1, x2, y2 in queries:
        kr = (x2 - x1 + 1).bit_length() - 1
        level = st[kr]
        packed = level[x1] | level[x2 - (1 << kr) + 1]

        width = y2 - y1 + 1
        folded = (packed >> (CELL * y1)) & col_mask[width]
        span = 1
        while span < width:
            folded |= folded >> (CELL * span)
            span <<= 1
        out.append(folded & MASK)
    return out


data = sys.stdin.buffer.read().split()
n, m = int(data[0]), int(data[1])
pack_row = struct.Struct("<%dI" % m).pack

packed_rows = []
at = 2
for _ in range(n):
    packed_rows.append(int.from_bytes(pack_row(*map(int, data[at:at + m])), "little"))
    at += m

q = int(data[at])
at += 1
nums = list(map(int, data[at:at + 4 * q]))
queries = [(nums[i] - 1, nums[i + 1] - 1, nums[i + 2] - 1, nums[i + 3] - 1)
           for i in range(0, 4 * q, 4)]

out_ = solve(n, m, packed_rows, queries)
sys.stdout.write("\n".join(map(str, out_)) + "\n")
