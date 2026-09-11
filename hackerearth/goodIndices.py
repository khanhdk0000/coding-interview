def solve(A):
    """Index i only needs its nearest strictly smaller element on each side to
    survive as its neighbour; everything between them must go. No smaller
    element on a side means i can never have a smaller neighbour there."""
    n = len(A)

    prev_smaller = [-1] * n
    stack = []
    for i, value in enumerate(A):
        while stack and A[stack[-1]] >= value:
            stack.pop()
        prev_smaller[i] = stack[-1] if stack else -1
        stack.append(i)

    next_smaller = [n] * n
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and A[stack[-1]] >= A[i]:
            stack.pop()
        next_smaller[i] = stack[-1] if stack else n
        stack.append(i)

    moves = []
    for i in range(n):
        left, right = prev_smaller[i], next_smaller[i]
        if left == -1 or right == n:
            moves.append(-1)
        else:
            moves.append((i - left - 1) + (right - i - 1))
    return moves


t = int(input())
out_ = []
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    out_.append(" ".join(map(str, solve(A))))

print("\n".join(out_))
