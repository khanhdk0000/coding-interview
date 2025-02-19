from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        isDuplicate = False
        while current.next and current.next.next:
            if current.next.val == current.next.next.val:
                current.next = current.next.next
                isDuplicate = True
            else:
                if isDuplicate:
                    current.next = current.next.next
                    isDuplicate = False
                    continue
                current = current.next
        if isDuplicate:
            current.next = current.next.next
        return dummy.next