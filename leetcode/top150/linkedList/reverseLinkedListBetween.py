from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next
        current = prev.next
        for _ in range(right - left):
            next = current.next
            current.next = next.next
            next.next = prev.next
            prev.next = next
        return dummy.next
    
    # bonus: reverse the whole linked list
    def reverseList(head):

    # Initialize three pointers: curr, prev and next
        curr = head
        prev = None

        # Traverse all the nodes of Linked List
        while curr is not None:

            # Store next
            nextNode = curr.next

            # Reverse current node's next pointer
            curr.next = prev

            # Move pointers one position ahead
            prev = curr
            curr = nextNode

        # Return the head of reversed linked list
        return prev