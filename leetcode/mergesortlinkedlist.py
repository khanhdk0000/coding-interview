# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def findMidHead(self, head: ListNode):
        slow = head
        fast = head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
        
    def merge(head1: ListNode, head2: ListNode):
        tmp = ListNode()
        res = tmp
        while head1 is not None and head2 is not None:
            if head1.val < head2.val:
                tmp.next = head1
                head1 = head1.next
            else:
                tmp.next = head2 
                head2 = head2.next
            tmp = tmp.next
        
        while head1 is not None:
            tmp.next = head1
            head1 = head1.next
            tmp = tmp.next

        while head2 is not None:
            tmp.next = head2
            head2 = head2.next
            tmp = tmp.next

        return res.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return head
        midHead = self.findMidHead(head)
        rightHead = midHead.next
        midHead.next = None
        left = self.sortList(head)
        right = self.sortList(rightHead)
        return self.merge(left, right)

        

