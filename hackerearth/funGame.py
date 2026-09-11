def solve(A):
    """A's copy only ever loses its front, B's copy only ever loses its back,
    so each list is just a shrinking window: A holds A[i:], B holds A[:j+1].
    Two pointers, one step per output, until a window runs out."""
    i, j = 0, len(A) - 1
    result = []
    while i < len(A) and j >= 0:
        if A[i] > A[j]:
            result.append(1)
            j -= 1
        elif A[i] < A[j]:
            result.append(2)
            i += 1
        else:
            result.append(0)
            i += 1
            j -= 1
    return result


n = int(input())
A = list(map(int, input().split()))

out_ = solve(A)
print(" ".join(map(str, out_)))
