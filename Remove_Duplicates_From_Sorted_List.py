class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0,next=head)
        slow = dummy
        while head :
            if head.next and head.val ==head.next.val :
                while head.next and head.val==head.next.val :
                    head=head.next
                slow.next=head.next
            else :
                slow=slow.next
            head=head.next
        return dummy.next
