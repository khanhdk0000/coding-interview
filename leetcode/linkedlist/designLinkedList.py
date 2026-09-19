class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None


class MyLinkedList:
    """LeetCode 707 - singly linked list with a sentinel head.

    The sentinel is a dummy node that always exists, so inserting or
    deleting at index 0 needs no special case: the node before index i
    is always reachable, even when i == 0.
    """

    def __init__(self):
        self.sentinel = Node(0)
        self.size = 0

    def _node_before(self, index: int) -> Node:
        """Node sitting just before `index`. index == 0 -> the sentinel."""
        prev = self.sentinel
        for _ in range(index):
            prev = prev.next
        return prev

    def get(self, index: int) -> int:
        if not 0 <= index < self.size:
            return -1
        return self._node_before(index).next.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        index = max(index, 0)  # spec: negative index means insert at head
        prev = self._node_before(index)
        node = Node(val)
        node.next = prev.next
        prev.next = node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if not 0 <= index < self.size:
            return
        prev = self._node_before(index)
        prev.next = prev.next.next
        self.size -= 1


def _to_list(ll: MyLinkedList):
    return [ll.get(i) for i in range(ll.size)]


def demo():
    ll = MyLinkedList()
    assert ll.get(0) == -1           # empty
    ll.addAtHead(1)
    ll.addAtTail(3)
    ll.addAtIndex(1, 2)              # 1 -> 2 -> 3
    assert _to_list(ll) == [1, 2, 3]
    assert ll.get(1) == 2
    ll.deleteAtIndex(1)              # 1 -> 3
    assert _to_list(ll) == [1, 3]
    ll.addAtIndex(5, 9)              # index > size, ignored
    ll.deleteAtIndex(7)              # out of range, ignored
    assert _to_list(ll) == [1, 3]
    ll.addAtIndex(2, 4)              # index == size, valid tail insert
    assert _to_list(ll) == [1, 3, 4]
    ll.addAtIndex(-1, 0)             # negative clamps to head
    assert _to_list(ll) == [0, 1, 3, 4]
    ll.deleteAtIndex(0)
    ll.deleteAtIndex(2)              # delete tail
    assert _to_list(ll) == [1, 3]
    print("ok")


if __name__ == "__main__":
    demo()
