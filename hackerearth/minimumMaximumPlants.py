import sys


def solve(n, m, broken_cols):
    """Rows are independent, and broken pots cut each row into runs of free
    cells. On a run of length L the largest non-adjacent set is ceil(L/2) and
    the smallest one that leaves no room for another plant is ceil(L/3)."""
    whole_row_max = (m + 1) // 2
    whole_row_min = (m + 2) // 3

    total_max = 0
    total_min = 0
    for row in range(n):
        if row not in broken_cols:
            total_max += whole_row_max
            total_min += whole_row_min
            continue

        prev = -1
        for col in sorted(broken_cols[row]) + [m]:
            run = col - prev - 1
            total_max += (run + 1) // 2
            total_min += (run + 2) // 3
            prev = col

    return total_max, total_min


data = sys.stdin.buffer.read().split()
n, m, b = int(data[0]), int(data[1]), int(data[2])
broken_cols = {}
for k in range(3, 3 + 2 * b, 2):
    broken_cols.setdefault(int(data[k]), set()).add(int(data[k + 1]))

out_ = solve(n, m, broken_cols)
print(*out_)
