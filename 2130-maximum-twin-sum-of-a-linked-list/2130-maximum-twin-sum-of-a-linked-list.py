class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head

        # Find middle of linked list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        ans = 0
        first = head
        second = prev

        # Calculate twin sums
        while second:
            ans = max(ans, first.val + second.val)
            first = first.next
            second = second.next

        return ans