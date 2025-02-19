from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        length = 0
        while current.next:
            current = current.next
            length += 1
        if length == 0:
            return head
        k %= length
        if k == 0:
            return head
        slow = dummy
        fast = dummy
        for i in range(k):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        fast.next = dummy.next
        dummy.next = slow.next
        slow.next = None
        return dummy.next