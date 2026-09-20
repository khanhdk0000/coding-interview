class SinglyLinkedListNode:
    # matches HackerRank's template: data only, no next arg
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


def deleteDuplicates(head):
    """Drop consecutive duplicates in a sorted list, in place. LeetCode 83."""
    node = head
    while node and node.next:
        if node.next.data == node.data:
            node.next = node.next.next  # skip dup, stay put: runs can be long
        else:
            node = node.next
    return head


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
    assert _to_list(deleteDuplicates(_build([1, 2, 2, 2, 3, 4, 4, 5]))) == [1, 2, 3, 4, 5]
    assert _to_list(deleteDuplicates(None)) == []
    assert _to_list(deleteDuplicates(_build([1]))) == [1]
    assert _to_list(deleteDuplicates(_build([1, 1, 1]))) == [1]  # all same
    assert _to_list(deleteDuplicates(_build([1, 2, 3]))) == [1, 2, 3]  # no dups
    assert _to_list(deleteDuplicates(_build([1, 1, 2, 2]))) == [1, 2]  # dup run at tail
    assert _to_list(deleteDuplicates(_build([-5, -5, 0, 0, 0]))) == [-5, 0]  # negatives
    print("ok")
