# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        curr=list1
        curr2=list1
        c=0
        while c != a-1 :
            curr=curr.next
            c +=1
        d=0
        while d != b :
            curr2=curr2.next
            d +=1
        #temp=curr.next
        #print(temp.val,temp2.val)
        #prev=curr
        temp2=curr2.next
        while list2.next :
            curr.next=list2
            list2=list2.next
            curr=curr.next
        list2.next=temp2
        return list1
