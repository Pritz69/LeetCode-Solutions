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
        if head is None :
            return None
        ptr=head
        while ptr :
            copy=Node(ptr.val,ptr.next)
            ptr.next=copy
            ptr=ptr.next.next
        ptr=head
        while ptr :
            copy=ptr.next
            copy.random=ptr.random.next if ptr.random else None
            ptr=copy.next # ptr=ptr.next.next
        ptr=head.next
        while ptr :
            ptr.next=ptr.next.next if ptr.next else None
            ptr=ptr.next 
        return head.next