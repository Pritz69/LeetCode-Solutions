# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head :
            return None
        if not head.next :
            return head
        st=[]
        curr=head
        while curr :
            while st and curr.val > st[-1] :
                st.pop()
            st.append(curr.val)
            curr=curr.next
        ans=ListNode(st[0])
        fans=ans
        for i in range(1,len(st)) :
            ans.next=ListNode(st[i])
            ans=ans.next
        return fans



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None

        head.next = self.removeNodes(head.next)
        
        if head.next and head.val < head.next.val:
            return head.next
        return head
            
