class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        import heapq

        # Create a max heap with counts and corresponding characters
        max_heap = []
        for count, char in [(-a, 'a'), (-b, 'b'), (-c, 'c')]:
            if count != 0:
                heapq.heappush(max_heap, (count, char))

        result = []
        while max_heap:
            count1, char1 = heapq.heappop(max_heap)
            # Check if the last two characters are the same as char1
            if len(result) >= 2 and result[-1] == result[-2] == char1:
                if not max_heap:
                    break  # No other character to use
                count2, char2 = heapq.heappop(max_heap)
                result.append(char2)
                count2 += 1  # Decrease the count (since counts are negative)
                if count2 != 0:
                    heapq.heappush(max_heap, (count2, char2))
                heapq.heappush(max_heap, (count1, char1))  # Push back char1
            else:
                result.append(char1)
                count1 += 1  # Decrease the count
                if count1 != 0:
                    heapq.heappush(max_heap, (count1, char1))

        return ''.join(result)
