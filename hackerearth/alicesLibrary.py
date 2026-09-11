def solve(s):
    """A shelf is done when its closing wall arrives, so keep one buffer per
    open shelf. Closing reverses the innermost buffer into its parent, which
    is exactly Alice working from the inside out."""
    shelves = [[]]
    for char in s:
        if char == "/":
            shelves.append([])
        elif char == "\\":
            inner = shelves.pop()
            inner.reverse()
            shelves[-1].extend(inner)
        else:
            shelves[-1].append(char)
    return "".join(shelves[0])


s = input().strip()

out_ = solve(s)
print(out_)
