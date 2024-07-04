/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeNodes(ListNode head) {
        ListNode prev=head;
        ListNode curr=head;
        while(curr != null)
        {
            if(curr.val==0)
            {
                int s=0;
                ListNode p=curr;
                curr=curr.next;
                int c=0;
                while(curr!=null && curr.val!=0)
                {
                    s += curr.val;
                    p=curr;
                    curr=curr.next;
                    c +=1;
                }
                if (s!=0 && c>=1)
                {
                    p.val=s;
                    prev.next=p;
                    prev=p;
                }
                else
                {
                    prev.next=curr;
                }
            }
        }
        return head.next;
    }
}
