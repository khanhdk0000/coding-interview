def CodelandUsernameValidation(strParam) -> bool:
    # 1. The username is between 4 and 25 characters.
    # 2. It must start with a letter.
    # 3. It can only contain letters, numbers, and the underscore character.
    # 4. It cannot end with an underscore character.
    if len(strParam) < 4 or len(strParam) > 25:
        return False
    if not strParam[0].isalpha():
        return False
    if strParam[-1] == '_':
        return False
    for char in strParam:
        if not (char.isalnum() or char == '_'):
            return False
    return True