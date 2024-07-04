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
        ListNode dummy=new ListNode(0);
        dummy.next=head;
        ListNode prev=dummy;
        ListNode curr=head;
        while(curr != null)
        {
            if(curr.val==0)
            {
                int s=0;
                curr=curr.next;
                int c=0;
                while(curr!=null && curr.val!=0)
                {
                    s += curr.val;
                    curr=curr.next;
                    c +=1;
                }
                if (c>=1)
                {
                    ListNode n=new ListNode(s);
                    prev.next=n;
                    prev=n;
                }
            }
        }
        return dummy.next;
    }
}
