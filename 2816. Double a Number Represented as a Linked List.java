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
    public ListNode doubleIt(ListNode head) {
        return addtwo(head,head);
    }
    public ListNode addtwo(ListNode l1,ListNode l2)
    {
        Stack<Integer>s1=new Stack<Integer>();
        Stack<Integer>s2=new Stack<Integer>();
        while (l1!=null)
        {
            s1.push(l1.val);
            s2.push(l1.val);
            l1=l1.next;
        }
        ListNode res=null;
        int c=0;
        while(!s1.isEmpty() || !s2.isEmpty())
        {
            int a=0;
            int b=0;
            if (!s1.isEmpty())
            {
                a=s1.pop();
            }
            if (!s2.isEmpty())
            {
                b=s2.pop();
            }
            int t=(a+b+c);
            ListNode tmp=new ListNode(t%10);
            c=t/10;
            if (res==null)
            {
                res=tmp;
            }
            else
            {
                tmp.next=res;
                res=tmp;
            }
        }
        if (c!=0)
        {
            ListNode tmp=new ListNode(c);
            tmp.next=res;
            res=tmp;
        }
        return res;
    }
}
