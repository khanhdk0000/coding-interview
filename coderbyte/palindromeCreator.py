'''
Challenge
function PalindromeCreator(str) take the str parameter being passed and determine if it is possible to create a palindromic string of at least 3 characters by removing 1 or 2 characters. For example: if str is "abjchba" then you can remove the characters jc to produce "abhba" which is a palindrome. For this example your program should return the two characters that were removed with no delimiter and in the order they appear in the string, so jc. If 1 or 2 characters cannot be removed to produce a palindrome, then return the string not possible. If the input string is already a palindrome, your program should return the string palindrome. 

The input will only contain lowercase alphabetic characters. Your program should always attempt to create the longest palindromic substring by removing 1 or 2 characters (see second sample test case as an example). The 2 characters you remove do not have to be adjacent in the string. 
Sample Test Cases
Input:"mmop"
Output:"not possible"

Input:"kjjjhjjj"
Output:"k"
'''

def PalindromeCreator(str):
    def isPalindrome(s):
        if len(s) < 3:
            return False
        return s == s[::-1]
    
    if len(str) < 3:
        return "not possible"
    
    if isPalindrome(str):
        return "palindrome"
    
    # Check by removing one character
    for i in range(len(str)):
        if isPalindrome(str[:i] + str[i+1:]):
            return str[i]
    
    # Check by removing two characters
    for i in range(len(str)):
        for j in range(i + 1, len(str)):
            if isPalindrome(str[:i] + str[i+1:j] + str[j+1:]):
                return str[i] + str[j]
    
    return "not possible"

print(PalindromeCreator("mmop"))  # Expected output: "not possible"
print(PalindromeCreator("kjjjhjjj"))  # Expected output: "k"
print(PalindromeCreator("abjchba"))  # Expected output: "jc"
print(PalindromeCreator("racecar"))  # Expected output: "palindrome"