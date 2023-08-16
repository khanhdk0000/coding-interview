from typing import List, Optional
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if (head == None or head.next == None):
            return False
        
        slow = head
        fast = head
        slow = slow.next
        fast = fast.next.next

        while (fast and fast.next):
            if (slow == fast):
                return True
            slow = slow.next
            fast = fast.next.next

        if (slow != fast):
            return False