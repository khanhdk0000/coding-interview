class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = self.next = None


class DLList:
    """Sentinel doubly linked list. head <-> oldest <-> ... <-> newest <-> tail."""

    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def empty(self) -> bool:
        return self.head.next is self.tail

    def oldest(self) -> Node:
        return self.head.next

    def append(self, node: Node) -> None:
        prev_node = self.tail.prev
        node.prev = prev_node
        node.next = self.tail
        prev_node.next = node
        self.tail.prev = node

    def remove(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev


class LFUCache:
    """LeetCode 460, no imports. All ops O(1).

    nodes[key]  -> Node (key, val, freq, list pointers)
    buckets[f]  -> DLList of every node with freq f, oldest first
    min_freq    -> smallest freq present, so eviction needs no search
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodes = {}
        self.buckets = {}
        self.min_freq = 0

    def _bucket(self, freq: int) -> DLList:
        if freq not in self.buckets:
            self.buckets[freq] = DLList()
        return self.buckets[freq]

    def _unlink(self, node: Node) -> None:
        """Pull node out of its freq bucket, dropping the bucket if it empties.
        On the eviction path min_freq may end up naming a missing bucket; put()
        resets it to 1 immediately after, so that is never observed."""
        f = node.freq
        bucket = self.buckets[f]
        bucket.remove(node)
        if bucket.empty():
            del self.buckets[f]
            if self.min_freq == f:
                self.min_freq = f + 1

    def _bump(self, node: Node) -> None:
        self._unlink(node)
        node.freq += 1
        self._bucket(node.freq).append(node)

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        node = self.nodes[key]
        self._bump(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return
        if key in self.nodes:
            node = self.nodes[key]
            node.val = value
            self._bump(node)
            return
        if len(self.nodes) >= self.capacity:
            victim = self.buckets[self.min_freq].oldest()
            self._unlink(victim)
            del self.nodes[victim.key]
        node = Node(key, value)
        self.nodes[key] = node
        self._bucket(1).append(node)
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
