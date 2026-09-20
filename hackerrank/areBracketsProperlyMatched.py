def areBracketsProperlyMatched(code_snippet: str) -> bool:
    """LeetCode 20, but non-bracket characters are ignored instead of pushed."""
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for c in code_snippet:
        if c in "([{":
            stack.append(c)
        elif c in pairs and (not stack or stack.pop() != pairs[c]):
            return False
    return not stack


if __name__ == "__main__":
    assert areBracketsProperlyMatched("if (a[0] > b[1]) { doSomething(); }") is True
    assert areBracketsProperlyMatched("int x = 42; // no brackets here") is True
    assert areBracketsProperlyMatched("() {} []") is True
    assert areBracketsProperlyMatched("") is True
    assert areBracketsProperlyMatched("(]") is False  # wrong type
    assert areBracketsProperlyMatched("([)]") is False  # crossed nesting
    assert areBracketsProperlyMatched("(") is False  # unclosed
    assert areBracketsProperlyMatched(")") is False  # closer with empty stack
    assert areBracketsProperlyMatched("a(b[c]{d}e)f") is True
    print("ok")
