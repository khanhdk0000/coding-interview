from typing import List


class Solution:
    def maximizeSquareHoleArea(
        self, n: int, m: int, hBars: List[int], vBars: List[int]
    ) -> int:
        def max_consecutive_span(bars: List[int]) -> int:
            """
            Find the maximum span achievable by removing a consecutive
            sequence of bars.

            For a consecutive run [x, x+1, ..., y], the hole spans
            from position (x-1) to (y+1), giving a length of y - x + 2.
            """
            bars.sort()
            max_span = 2  # minimum: remove just 1 bar → span of 2
            streak_start = 0  # index where current consecutive run begins

            for i in range(1, len(bars)):
                if bars[i] != bars[i - 1] + 1:
                    # streak broken — reset
                    streak_start = i
                # span = bars[i] - bars[streak_start] + 2
                max_span = max(max_span, bars[i] - bars[streak_start] + 2)

            return max_span

        h = max_consecutive_span(hBars)  # max vertical side length
        v = max_consecutive_span(vBars)  # max horizontal side length

        side = min(h, v)
        return side * side
