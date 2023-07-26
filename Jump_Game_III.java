class Solution {
    public boolean canReach(int[] arr, int start) {
        int n=arr.length;
        Queue<Integer>q=new LinkedList<>();
        q.offer(start);
        while (!q.isEmpty())
        {
            int size=q.size();
            while (size-- >0)
            {
                int v=q.poll();
                if (v-arr[v]>=0)
                {
                    if (arr[v-arr[v]]==0)
                    {
                        return true;
                    }
                    else if(arr[v-arr[v]]>0)
                    {
                        q.offer(v-arr[v]);
                    }
                }
                if(v+arr[v]<n)
                {
                    if(arr[v+arr[v]]==0)
                    {
                        return true;
                    }
                    else if(arr[v+arr[v]]>0)
                    {
                        q.offer(v+arr[v]);
                    }
                }
                arr[v]=-1;
            }
        }
        return false;
    }
}
