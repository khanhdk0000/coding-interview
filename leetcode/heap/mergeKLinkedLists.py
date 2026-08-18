# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ListNode.__lt__ = lambda self, other: self.val < other.val
        heap = []
        for head in lists:
            if head:
                heapq.heappush(heap, head)

        dummy = ListNode(-1)
        curr = dummy
        while heap:
            smallest_node = heapq.heappop(heap)
            curr.next = smallest_node
            curr = curr.next
            if smallest_node.next:
                heapq.heappush(heap, smallest_node.next)
        return dummy.next