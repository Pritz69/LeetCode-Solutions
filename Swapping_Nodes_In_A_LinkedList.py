# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        c=0
        curr=head
        while(curr) :
            c +=1
            curr=curr.next
        end=c-k
        l=head
        while(k-1) :
            l=l.next
            k -=1
        r=head
        while(end) :
            r=r.next
            end -=1
        l.val,r.val = r.val,l.val
        return head
