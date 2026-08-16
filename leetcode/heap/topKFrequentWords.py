from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freqs = Counter(words)
        max_heap = [Pair(value, freq) for value, freq in freqs.items()]
        heapq.heapify(max_heap)
        return [heapq.heappop(max_heap).value for _ in range(k)]

class Pair:
    def __init__(self, value, freq):
        self.value = value
        self.freq = freq

    def __lt__(self, other):
        if self.freq == other.freq:
            return self.value < other.value
        return self.freq > other.freq

    
## time complexity: O(n+k log(n))