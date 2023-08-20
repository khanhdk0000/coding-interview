# Definition for singly-linked list.
from typing import List, Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res, leftOver = ListNode(), 0
        res.next = ListNode()
        start = res.next
        
        while l1 or l2:
            val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + leftOver
            start.val = val % 10
            leftOver = val // 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            if l1 or l2:
                start.next = ListNode()
                start = start.next
        
        if leftOver > 0:
            start.next = ListNode(leftOver)
            start = start.next 
        
        return res.next