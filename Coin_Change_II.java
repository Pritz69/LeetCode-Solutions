class Solution {
    public int memoize(int amount,int coins[],int dp[][],int ind,int sum,int n)
    {
        if(sum==amount)
        {
            return 1;
        }
        if(sum>amount || ind==n)
        {
            return 0;
        }
        if(dp[ind][sum] != -1)
        {
            return dp[ind][sum];
        }
        int take=memoize(amount,coins,dp,ind,sum+coins[ind],n);
        int nottake=memoize(amount,coins,dp,ind+1,sum,n);
        int total=take+nottake;
        dp[ind][sum]=total;
        return total;
    }
    public int change(int amount, int[] coins) {
        int n=coins.length;
        int dp[][]=new int[n][amount+1];
        for(int a[]:dp)
        {
            Arrays.fill(a,-1);
        }
        int ans=memoize(amount,coins,dp,0,0,n);
        return ans;
    }
}
