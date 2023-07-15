class Solution {
    public int binsearch(int [][]events,int k)
    {
        int l=0;
        int r=events.length-1;
        int ans=events.length;
        while (l<=r)
        {
            int m=(l+r)/2;
            if(events[m][0]>k)
            {
                ans=m;
                r=m-1;
            }
            else
            {
                l=m+1;
            }
        }
        return ans;
    }
    public int dfs(int index,int count,int [][]events,int [][]dp)
    {
        if (count==0 || index==events.length)
        {
            return 0;
        }
        if (dp[count][index]!=-1)
        {
            return dp[count][index];
        }
        int nextind=binsearch(events,events[index][1]);
        dp[count][index]=Math.max((events[index][2] + dfs(nextind,count-1,events,dp)),dfs(index+1,count,events,dp));
        return dp[count][index];
    }
    public int maxValue(int[][] events, int k) {
        int n=events.length;
        Arrays.sort(events, (a,b)-> a[0]-b[0]);
        int dp[][]=new int[k+1][n];
        for (int r[]:dp)
        {
            Arrays.fill(r,-1);
        }
        return dfs(0,k,events,dp);
    }
}
