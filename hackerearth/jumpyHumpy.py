def solve(A):
    """Every journey is forced: from a building you jump to the next taller one
    on its right, so the route from i is i plus the whole route from its next
    greater element. Walk right to left with a monotonic stack and each answer
    is one xor onto an already solved suffix."""
    stack = []
    stamina = [0] * len(A)
    for i in range(len(A) - 1, -1, -1):
        while stack and A[stack[-1]] <= A[i]:
            stack.pop()
        stamina[i] = A[i] ^ (stamina[stack[-1]] if stack else 0)
        stack.append(i)
    return max(stamina)


n = int(input())
A = list(map(int, input().split()))

out_ = solve(A)
print(out_)
