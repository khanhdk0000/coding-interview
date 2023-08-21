# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseLinkedList(self, head: Optional[ListNode], num):
        prev = None
        current = head

        while current is not None and num > 0:
            # Store the next node
            next_node = current.next

            # Reverse the next pointer
            current.next = prev

            # Move to the next nodes
            prev = current
            current = next_node
            num -= 1
        return prev, current

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        i = 1
        prev = None
        headNode = head
        while i != left:
            prev = headNode
            headNode = headNode.next
            i += 1
        copyHeadNode = headNode
        reverseHead, nextNode = self.reverseLinkedList(headNode, right - left + 1)
        if prev:
            prev.next = reverseHead
        else:
            head = reverseHead
        copyHeadNode.next = nextNode
        return head