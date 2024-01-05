class Solution {
    public int lengthOfLIS(int[] nums) {
        int dp[]=new int[nums.length +1];
        int m=0;
        for(int i=0;i<nums.length;i++)
        {
            dp[i]=1;
            for(int j=0;j<i;j++)
            {
                if (nums[j]<nums[i])
                {
                    dp[i]=Math.max(dp[i],dp[j]+1);
                }
            }
            m=Math.max(dp[i],m);
        }
        return m;
    }
}
