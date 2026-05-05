from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        trailer = dummy
        leader = dummy
        for i in range(n):
            leader = leader.next
            if not leader:
                return head
        while leader.next:
            trailer = trailer.next
            leader = leader.next
        trailer.next = trailer.next.next
        return dummy.next