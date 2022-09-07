class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy=ListNode(next=head)
        prev,curr=dummy,head
        while curr :
            nxt=curr.next
            if curr.val==val :
                prev.next=nxt 
            else :
                prev=curr
            curr=nxt
        return dummy.next
