# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        s=set(nums)
        p=ListNode(0)
        ans=p
        curr=head
        while curr :
            while curr and curr.val in s :
                curr=curr.next
            p.next=curr
            p=curr
            if curr : curr=curr.next
        return ans.next