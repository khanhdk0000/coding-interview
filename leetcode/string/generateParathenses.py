from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res: List[str] = []

        def backtrack(cur: List[str], open_left: int, close_left: int) -> None:
            if open_left == 0 and close_left == 0:
                res.append(''.join(cur))
                return

            # try to place '('
            if open_left > 0:
                cur.append('(')
                backtrack(cur, open_left - 1, close_left)
                cur.pop()

            # try to place ')'
            if close_left > open_left:   # there are unmatched '('
                cur.append(')')
                backtrack(cur, open_left, close_left - 1)
                cur.pop()

        backtrack([], n, n)
        return res
