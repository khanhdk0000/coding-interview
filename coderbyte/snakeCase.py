# // For this challenge you will be converting a string into snake case format.
# /*
# have the function SnakeCase(str) take the str parameter being passed and return it in proper snake case format where each word is lowercased and separated from adjacent words via an underscore. The string will only contain letters and some combination of delimiter punctuation characters separating each word.

# For example: if str is "BOB loves-coding" then your program should return the string bob_loves_coding.
# */
import re
def SnakeCase(s):
    # Split the string into words using non-letter characters as separators
    words = re.split(r'[^a-zA-Z]+', s)

    # Filter out any empty strings in case of multiple delimiters
    words = [word for word in words if word]

    # Return snake_case format
    if not words:
        return ""

    # Join the words with underscores and convert to lowercase
    return '_'.join(word.lower() for word in words)

print(SnakeCase("BOB loves-coding"))  # Output: bob_loves_coding
print(SnakeCase("cats AND*Dogs-are Awesome"))  # Output: cats_and_dogs_are_awesome
print(SnakeCase("a b c d-e-f%g"))  # Output: a_b_c_d_e_f_g