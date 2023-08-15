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
    public ListNode partition(ListNode head, int x) {
        ListNode left=new ListNode();
        ListNode curr1=left;
        ListNode right=new ListNode();
        ListNode curr2=right;
        while(head != null)
        {
            if(head.val < x)
            {
                ListNode tmp=new ListNode(head.val);
                left.next=tmp;
                left=tmp;
            }
            else
            {
                ListNode tmp=new ListNode(head.val);
                right.next=tmp;
                right=tmp;
            }
            head=head.next;
        }
        left.next=curr2.next;
        return curr1.next;
    }
}
