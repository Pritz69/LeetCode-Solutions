# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cnt=0
        tmp=head
        while tmp :
            tmp=tmp.next
            cnt +=1
        if cnt==n :
            return head.next
        ans=cnt-n
        p,c=ListNode(0),head
        while ans :
            p=c
            c=c.next
            ans -=1
        p.next=c.next
        return head
