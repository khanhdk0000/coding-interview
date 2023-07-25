import re
def main():
    password = input()
    if process(password):
        print("YES")
    else:
        print("NO")

def process(password):
    if not re.search("[a-z]", password) or not re.search("[A-Z]", password):
        return False

    # At least 1 number between [0-9]
    if not re.search("[0-9]", password):
        return False

    # At least 1 character from [$#@]
    if not re.search("[$#@]", password):
        return False

    # Minimum length 6 characters, maximum length 16 characters
    if len(password) < 6 or len(password) > 16:
        return False

    return True
main()