class SinglyLinkedListNode:
    # matches HackerRank's template: data only, no next arg
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


def removeKthNodeFromEnd(head, k):
    """Remove node at index k from the end, 0-indexed. Invalid k returns head unchanged."""
    fast = head
    steps = k + 1
    while steps and fast:  # flat loop: no nesting for editors to mangle
        fast = fast.next
        steps -= 1
    if steps:
        return head  # ran out of nodes: k >= length, nothing to remove
    dummy = SinglyLinkedListNode(0)
    dummy.next = head
    slow = dummy
    while fast:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return dummy.next


def _build(values):
    head = None
    for v in reversed(values):
        node = SinglyLinkedListNode(v)
        node.next = head
        head = node
    return head


def _to_list(node):
    out = []
    while node:
        out.append(node.data)
        node = node.next
    return out


if __name__ == "__main__":
    assert _to_list(removeKthNodeFromEnd(_build([5, 6, 7, 8]), 3)) == [6, 7, 8]  # removes head
    assert _to_list(removeKthNodeFromEnd(_build([5]), 1)) == [5]  # k out of range
    assert _to_list(removeKthNodeFromEnd(_build([1, 2]), 0)) == [1]  # removes tail
    assert _to_list(removeKthNodeFromEnd(_build([5]), 0)) == []  # only node
    assert _to_list(removeKthNodeFromEnd(None, 0)) == []  # empty list
    assert _to_list(removeKthNodeFromEnd(_build([1, 2, 3]), 1)) == [1, 3]  # middle
    assert _to_list(removeKthNodeFromEnd(_build([1, 2, 3]), 10**9)) == [1, 2, 3]  # huge k, no hang
    print("ok")
