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
        ListNode prev=head;
        ListNode curr=head.next;
        ListNode nxt=curr.next;
        ArrayList<Integer>a=new ArrayList<>();
        int c=1;
        while (curr != null)
        {
            c +=1;
            if (nxt !=null)
            {
                if ((curr.val < prev.val && curr.val < nxt.val) || (curr.val > prev.val && curr.val > nxt.val))
                {
                    a.add(c);
                }
            }
            prev=curr;
            curr=nxt;
            if (nxt!=null)
                nxt=nxt.next;
        }
        if (a.size()<2)
        {
            ans[0]=-1;
            ans[1]=-1;
            return ans;
        }
        ans[1]=a.get(a.size()-1)-a.get(0);
        int m=ans[1];
        for(int i=1;i<a.size();i++)
        {
            m=Math.min(m,a.get(i)-a.get(i-1));
        }
        ans[0]=m;
        return ans;
    }
}