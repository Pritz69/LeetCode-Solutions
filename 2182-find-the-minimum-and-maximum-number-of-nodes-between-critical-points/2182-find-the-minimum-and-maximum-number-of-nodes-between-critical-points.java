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
    public int[] nodesBetweenCriticalPoints(ListNode head) {
        int ans[]=new int[2];
        ans[0]=-1;
        ans[1]=-1;
        ListNode prev=head;
        ListNode curr=head.next;
        ListNode nxt=curr.next;
        int c=1;
        int f=0;
        int first=0;
        int minb=Integer.MAX_VALUE;
        int prevb=0;
        int last=0;
        while (curr != null)
        {
            c +=1;
            if ( (nxt !=null) && ( (curr.val < prev.val && curr.val < nxt.val) || (curr.val > prev.val && curr.val > nxt.val) ) )
            {
                if(f==0)
                {
                    first=c;
                    f=1;
                    prevb=c;
                }
                else
                {
                    minb=Math.min(minb,c-prevb);
                    prevb=c;
                    last=c;
                }
            }
            prev=curr;
            curr=nxt;
            if (nxt!=null)
                nxt=nxt.next;
        }
        ans[1]=last-first;
        ans[0]=minb;
        if(ans[0] <=0 || ans[1] <=0)
        {
            ans[0]=-1;ans[1]=-1;
            return ans;
        }
        return ans;
    }
}