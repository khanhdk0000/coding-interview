from collections import Counter


def isValid(s: str) -> str:
    cnt = Counter(s)
    if len(set(cnt.values())) == 1:
        return "YES"
    # ponytail: try removing one of each distinct char; at most 26 tries, O(26 * 26)
    for c in cnt:
        cnt[c] -= 1
        if len({v for v in cnt.values() if v > 0}) == 1:
            return "YES"
        cnt[c] += 1
    return "NO"


if __name__ == '__main__':
    assert isValid("abc") == "YES"
    assert isValid("abcc") == "YES"
    assert isValid("abccc") == "NO"
    assert isValid("aabbcd") == "NO"
    assert isValid("aabbccddeefghi") == "NO"
    assert isValid("abcdefghhgfedecba") == "YES"
    assert isValid("aabbc") == "YES"   # remove the lone c entirely
    assert isValid("aaab") == "YES"    # remove lone b, only a's left
    assert isValid("aaaabb") == "NO"
    assert isValid("a") == "YES"
    print("ok")
