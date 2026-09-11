def solve(digits, k):
    """Scan left to right keeping a non-increasing stack: a digit smaller than
    the one after it is always worth deleting, since promoting the bigger digit
    to an earlier place beats anything the smaller one can win later."""
    keep = len(digits) - k
    stack = []
    for digit in digits:
        while k and stack and stack[-1] < digit:
            stack.pop()
            k -= 1
        stack.append(digit)
    return "".join(stack[:keep])


digits = input().strip()
k = int(input())

out_ = solve(digits, k)
print(out_)
