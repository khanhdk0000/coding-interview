from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while head:
            tail = prev
            for i in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next
            nextHead = tail.next
            head, tail = self.reverse(head, tail)
            prev.next = head
            tail.next = nextHead
            prev = tail
            head = nextHead
        return dummy.next
    def reverse(self, head, tail):
        prev = tail.next
        current = head
        while prev != tail:
            next = current.next
            current.next = prev
            prev = current
            current = next
        return tail, head