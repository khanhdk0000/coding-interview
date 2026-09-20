def isAlphabeticPalindrome(code: str) -> bool:
    """Palindrome check over letters only, case-insensitive. Digits/symbols dropped."""
    letters = [c for c in code.lower() if c.isalpha()]
    return letters == letters[::-1]


if __name__ == "__main__":
    assert isAlphabeticPalindrome("A1b2B!a") is True
    assert isAlphabeticPalindrome("Z") is True
    assert isAlphabeticPalindrome("abc123cba") is True
    assert isAlphabeticPalindrome("") is True
    assert isAlphabeticPalindrome("12345") is True  # no letters
    assert isAlphabeticPalindrome("ab") is False
    assert isAlphabeticPalindrome("race a car") is False
    print("ok")
