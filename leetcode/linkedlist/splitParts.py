# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List, Optional
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # Step 1: Count the number of nodes in the linked list
        count = 0
        current = head
        while current:
            count += 1
            current = current.next

        # Step 2: Calculate the size of each part and the number of longer parts
        part_size = count // k
        longer_parts = count % k

        # Step 3: Create an array to hold the resulting parts
        result = [None] * k

        # Step 4: Split the linked list into parts
        current = head
        for i in range(k):
            result[i] = current
            size = part_size + (1 if i < longer_parts else 0)

            # Move to the end of the current part
            for j in range(size - 1):
                if current:
                    current = current.next

            # Disconnect the current part from the next part
            if current:
                next_part = current.next
                current.next = None
                current = next_part

        return result