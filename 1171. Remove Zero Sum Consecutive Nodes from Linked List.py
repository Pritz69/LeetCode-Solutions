# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        psum=0
        d={}
        dummy=ListNode(0,head)
        d[0]=dummy
        while head :
            psum += head.val
            if psum in d :
                temp=d[psum]
                start=temp
                ps=psum
                while temp != head :
                    temp=temp.next
                    ps +=temp.val
                    if temp != head :
                        d.pop(ps)
                start.next=head.next
            else :
                d[psum]=head
            head=head.next
        return dummy.next
