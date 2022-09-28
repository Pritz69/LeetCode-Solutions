class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        left=dummy
        right=head
        while n != 0 :
            right = right.next
            n -=1
        while right :
            left=left.next
            right=right.next
        left.next=left.next.next
        return dummy.next
