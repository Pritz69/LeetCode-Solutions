# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        curr=head
        n=0
        while curr :
            n +=1
            curr=curr.next
        no=n // k
        ex=n % k
        l=[]
        curr=head
        while k >0 :
            if ex >0 :
                t=no+1
                ex -=1
            else :
                t=no
            l.append(head)
            last=None
            while t > 0 :
                last=head
                head=head.next
                t -=1
            if last :
                last.next=None
            k -=1
        return l
