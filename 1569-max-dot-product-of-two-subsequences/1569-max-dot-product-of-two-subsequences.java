class Solution {
    public int maxDotProduct(int[] nums1, int[] nums2) {
        int fmin=Integer.MAX_VALUE;
        int fmax=Integer.MIN_VALUE;
        int smin=Integer.MAX_VALUE;
        int smax=Integer.MIN_VALUE;
        for(int n:nums1)
        {
            fmin=Math.min(fmin,n);
            fmax=Math.max(fmax,n);
        }
        for(int n:nums2)
        {
            smin=Math.min(smin,n);
            smax=Math.max(smax,n);
        }
        if ( (fmax < 0 && smin > 0) || (smax<0 && fmin >0) )
        {
            return Math.max(fmax*smin ,  smax*fmin);
        }
        int dp[][]=new int[nums1.length +1][nums2.length +1];
        for(int i=1;i<=nums1.length;i++)
        {
            for(int j=1;j<=nums2.length;j++)
            {
                int v= dp[i-1][j-1] + ( nums1[i-1]*nums2[j-1] );
                dp[i][j] = Math.max( v , Math.max(dp[i-1][j],dp[i][j-1])) ;
            }
        }
        return dp[nums1.length][nums2.length];
    }
}