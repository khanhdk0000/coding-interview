class Solution:
    def minimumSteps(self, s: str) -> int:
        total_zero = s.count('0')  # Total number of white balls
        count_zero_right = total_zero
        steps = 0
        for c in s:
            if c == '1':
                steps += count_zero_right
            else:
                count_zero_right -= 1
        return steps
