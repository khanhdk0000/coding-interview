def solve(monsters):
    """Survivors always sit in a strictly decreasing stack: anyone weaker than
    a later arrival is already gone. So each monster pops while the top is at
    most as strong, pushes itself, and the answer is the stack size."""
    alive = []
    counts = []
    for strength in monsters:
        while alive and alive[-1] <= strength:
            alive.pop()
        alive.append(strength)
        counts.append(len(alive))
    return counts


# data = sys.stdin.buffer.read().split()
# t = int(data[0])
# at = 1
# out_ = []
# for _ in range(t):
#     n = int(data[at])
#     monsters = list(map(int, data[at + 1:at + 1 + n]))
#     at += 1 + n
#     out_.append(" ".join(map(str, solve(monsters))))
#
# sys.stdout.write("\n".join(out_) + "\n")

t = int(input())
out_ = []
for _ in range(t):
    n = int(input())
    monsters = list(map(int, input().split()))
    out_.append(" ".join(map(str, solve(monsters))))

print("\n".join(out_))
