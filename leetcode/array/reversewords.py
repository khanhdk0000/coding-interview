from typing import List

class Solution:
    def reverseWords(self, s: str) -> str:
        words = self.splitWords(s)
        return ' '.join(words[::-1])

    def splitWords(self, s: str)-> List[str]:
        words = []
        current_word = ""
        for char in s:
            if char != ' ':
                current_word += char
            else:
                if current_word:
                    words.append(current_word)
                current_word = ""

        if current_word:
            words.append(current_word)

        return words


sol = Solution()
input = "EPY2giL"

print(sol.reverseWords(input))