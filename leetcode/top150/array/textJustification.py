from typing import List
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i = 0
        while i < len(words):
            j = i + 1
            line = len(words[i])
            while j < len(words) and line + len(words[j]) + j - i <= maxWidth:
                line += len(words[j])
                j += 1
            space = maxWidth - line
            if j - i == 1 or j == len(words):
                res.append(words[i] + ' ' * space)
                i = j
                continue
            avg, extra = divmod(space, j - i - 1)
            for k in range(extra):
                words[i + k] += ' '
            res.append((' ' * avg).join(words[i:j]))
            i = j
        return res

sol = Solution()
print(sol.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))