class Solution {
    public int helper(int []arr,int d,int ind,int []dp)
    {
        int res=1;
        if(dp[ind] >0)
        {
            return dp[ind];
        }
        for(int i=ind-1;i>=Math.max(0,ind-d) && arr[ind] > arr[i]; i--)
        {
            res=Math.max(res, 1+helper(arr,d,i,dp));
        }
        for(int i=ind+1;i<=Math.min(arr.length-1,ind+d) && arr[ind] > arr[i];i++)
        {
            res=Math.max(res, 1+helper(arr,d,i,dp));
        }
        dp[ind]=res;
        return res;
    }
    public int maxJumps(int[] arr, int d) {
        int n=arr.length;
        int ans=1;
        int dp[]=new int[n];
        for(int i=0;i<n;i++)
        {
            ans=Math.max(ans,helper(arr,d,i,dp));
        }
        return ans;
    }
}
