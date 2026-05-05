# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        LeetCode 21 - Merge Two Sorted Lists

        Approach: Iterative with dummy head
        - Use a dummy node as the head of the result to avoid edge-case handling.
        - At each step, attach the smaller of the two current nodes directly
          (no new node allocation — just relink existing nodes).
        - Once one list is exhausted, point cur.next to the remaining list
          directly (no need to loop — it's already sorted and linked).

        Time Complexity : O(n + m)  — each node is visited at most once
        Space Complexity: O(1)      — relinks existing nodes; no new allocations
        """
        dummy = ListNode()
        cur = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        # Attach the remaining tail directly — already sorted and linked
        cur.next = list1 if list1 else list2

        return dummy.next
