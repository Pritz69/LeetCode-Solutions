class Solution {
    public int findTheWinner(int n, int k) {
        Queue<Integer>qu=new LinkedList<>() ;
        for(int i=1;i<=n;i++)
        {
            qu.offer(i);
        }
        while (qu.size()!=1)
        {
            for(int i=1;i<=k-1;i++)
            {
                qu.offer(qu.poll());
            }
            qu.poll();
        }
        return qu.poll();
    }
}
