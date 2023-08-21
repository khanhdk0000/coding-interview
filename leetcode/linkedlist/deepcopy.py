"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        res = Node(0)
        nodeMap = {}
        arrNode = []
        i = 0
        head2 = head
        res.next = Node(0)
        resNode = res.next
        while head:
            nodeMap[head] = i
            resNode.val = head.val
            head = head.next
            arrNode.append(resNode)
            if head:
                resNode.next = Node(0)
                resNode = resNode.next
            i += 1

        resNode = res.next  
        while head2:
            if head2.random is None:
                resNode.random = None
            else:
                pos = nodeMap[head2.random]
                resNode.random = arrNode[pos]
            head2 = head2.next
            resNode = resNode.next

        return res.next
