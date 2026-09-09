from collections import defaultdict, OrderedDict


class LFUCache:
    """LeetCode 460. All ops O(1).

    Three structures kept in sync:
      vals[key]      -> value
      freqs[key]      -> how many times key was touched
      buckets[f]      -> OrderedDict of keys with freq f, oldest first (LRU inside a tie)
      min_freq        -> smallest freq currently present, so eviction is O(1)
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.vals = {}
        self.freqs = {}
        self.buckets = defaultdict(OrderedDict)
        self.min_freq = 0

    def _bump(self, key: int) -> None:
        """Move key from bucket f to bucket f+1."""
        f = self.freqs[key]
        del self.buckets[f][key]
        if not self.buckets[f]:
            del self.buckets[f]
            if self.min_freq == f:
                self.min_freq = f + 1
        self.freqs[key] = f + 1
        self.buckets[f + 1][key] = None  # appended last => most recently used

    def get(self, key: int) -> int:
        if key not in self.vals:
            return -1
        self._bump(key)
        return self.vals[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return
        if key in self.vals:
            self.vals[key] = value
            self._bump(key)
            return
        if len(self.vals) >= self.capacity:
            evict, _ = self.buckets[self.min_freq].popitem(last=False)  # oldest of least frequent
            if not self.buckets[self.min_freq]:
                del self.buckets[self.min_freq]
            del self.vals[evict]
            del self.freqs[evict]
        self.vals[key] = value
        self.freqs[key] = 1
        self.buckets[1][key] = None
        self.min_freq = 1


if __name__ == "__main__":
    # LeetCode 460 sample
    c = LFUCache(2)
    c.put(1, 1)
    c.put(2, 2)
    assert c.get(1) == 1          # freq: 1->2, 2->1
    c.put(3, 3)                   # evicts 2 (least frequent)
    assert c.get(2) == -1
    assert c.get(3) == 3          # freq: 3->2
    c.put(4, 4)                   # tie freq 2 vs 2 -> evict 1 (older)
    assert c.get(1) == -1
    assert c.get(3) == 3
    assert c.get(4) == 4

    # LRU tie-break inside same freq
    d = LFUCache(2)
    d.put(1, 1)
    d.put(2, 2)
    d.put(3, 3)                   # all freq 1 -> evict 1 (oldest)
    assert d.get(1) == -1
    assert d.get(2) == 2

    # update existing counts as a use
    e = LFUCache(2)
    e.put(1, 1)
    e.put(2, 2)
    e.put(1, 10)                  # freq 1->2
    e.put(3, 3)                   # evicts 2
    assert e.get(2) == -1
    assert e.get(1) == 10

    assert LFUCache(0).get(1) == -1
    print("ok")
