from typing import Optional
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        dummy = Node(0)
        current = dummy
        mapping = {}
        while head:
            if head not in mapping:
                mapping[head] = Node(head.val)
            current.next = mapping[head]
            if head.random:
                if head.random not in mapping:
                    mapping[head.random] = Node(head.random.val)
                current.next.random = mapping[head.random]
            head = head.next
            current = current.next
        return dummy.next
