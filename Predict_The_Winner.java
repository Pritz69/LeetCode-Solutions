class Solution {
    public int recur(int nums[],int i,int j,int dp[][])
    {
        if ( i > j )
        {
            return 0;
        }
        if (dp[i][j] != -1)
        {
            return dp[i][j];
        }
        int left = nums[i] + Math.min(recur(nums,i+2,j,dp),recur(nums,i+1,j-1,dp));
        int right= nums[j] + Math.min(recur(nums,i,j-2,dp),recur(nums,i+1,j-1,dp));
        dp[i][j]= Math.max(left,right);
        return dp[i][j];
    }
    public boolean PredictTheWinner(int[] nums) {
        int n=nums.length;
        int dp[][]=new int[n][n];
        for (int x[]:dp)
        {
            Arrays.fill(x,-1);
        }
        int s=0;
        for(int x:nums)
        {
            s +=x;
        }
        int A = recur(nums,0,n-1,dp);
        int B = s - A ;
        return A >= B ;
    }
}
