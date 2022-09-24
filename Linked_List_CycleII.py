class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head :
            return
        slow,fast=head,head 
        while fast.next and fast.next.next :
            slow=slow.next
            fast=fast.next.next
            if fast==slow :
                break
        if not fast.next or not fast.next.next :
            return
        
        slow2=head
        while fast.next :
            if slow2==fast :
                return fast
            fast=fast.next
            slow2=slow2.next
        return 
