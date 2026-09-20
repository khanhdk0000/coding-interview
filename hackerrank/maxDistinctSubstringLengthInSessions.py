def maxDistinctSubstringLengthInSessions(sessionString: str) -> int:
    """LeetCode 3 per session. '*' resets the window (no substring crosses it)."""
    seen = {}
    best = 0
    left = 0
    for right, c in enumerate(sessionString):
        if c == "*":
            seen.clear()  # ponytail: <=26 keys, clear is cheap
            left = right + 1
            continue
        if seen.get(c, -1) >= left:
            left = seen[c] + 1
        seen[c] = right
        best = max(best, right - left + 1)
    return best


if __name__ == "__main__":
    assert maxDistinctSubstringLengthInSessions("abcabcbb") == 3
    assert maxDistinctSubstringLengthInSessions("*") == 0
    assert maxDistinctSubstringLengthInSessions("") == 0
    assert maxDistinctSubstringLengthInSessions("aa") == 1
    assert maxDistinctSubstringLengthInSessions("***") == 0
    assert maxDistinctSubstringLengthInSessions("ab*abcd*xy") == 4  # best session is "abcd"
    assert maxDistinctSubstringLengthInSessions("abc*") == 3
    assert maxDistinctSubstringLengthInSessions("*abc") == 3
    assert maxDistinctSubstringLengthInSessions("pwwkew") == 3
    print("ok")
