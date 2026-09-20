class SinglyLinkedListNode:
    # matches HackerRank's template: data only, no next arg
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


def extractAndAppendSponsoredNodes(head):
    """Move even-indexed nodes to the end in reverse order. One pass, no extra list."""
    odd_dummy = SinglyLinkedListNode(0)
    odd_tail = odd_dummy
    rev = None  # even-indexed nodes, reversed by prepending
    i = 0
    node = head
    while node:
        nxt = node.next
        if i % 2:
            odd_tail.next = node
            odd_tail = node
        else:
            node.next = rev
            rev = node
        node = nxt
        i += 1
    odd_tail.next = rev
    return odd_dummy.next


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
    assert _to_list(extractAndAppendSponsoredNodes(_build([10, 20, 30, 40, 50, 60]))) == [20, 40, 60, 50, 30, 10]
    assert _to_list(extractAndAppendSponsoredNodes(_build([42]))) == [42]
    assert _to_list(extractAndAppendSponsoredNodes(_build([1, 2]))) == [2, 1]
    assert _to_list(extractAndAppendSponsoredNodes(None)) == []
    assert _to_list(extractAndAppendSponsoredNodes(_build([1, 2, 3]))) == [2, 3, 1]
    assert _to_list(extractAndAppendSponsoredNodes(_build([1, 2, 3, 4, 5]))) == [2, 4, 5, 3, 1]
    print("ok")
