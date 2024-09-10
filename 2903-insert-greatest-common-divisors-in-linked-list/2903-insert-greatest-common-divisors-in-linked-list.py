# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a,b) :
            if b==0 :
                return a
            return gcd(b,a%b)
        curr=head
        while curr and curr.next :
            l=gcd(curr.val,curr.next.val)
            nxt=curr.next
            node=ListNode(l)
            curr.next=node
            node.next=nxt
            curr=nxt
        return head