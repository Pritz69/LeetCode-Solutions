class Solution {
    public boolean isInterleave(String s1, String s2, String s3) {
        int n=s1.length();
        int m=s2.length();
        if(n+m != s3.length())
        {
            return false;
        }
        Boolean dp[][]=new Boolean[n+1][m+1];
        for (Boolean i[]:dp)
        {
            Arrays.fill(i,false);
        }
        dp[n][m]=true;
        for(int i=n;i>=0;i--)
        {
            for(int j=m;j>=0;j--)
            {
                if((j<m) && s2.charAt(j)==s3.charAt(i+j) && dp[i][j+1]==true)
                {
                    dp[i][j]=true;
                }
                if((i<n) && s1.charAt(i)==s3.charAt(i+j) && dp[i+1][j]==true)
                {
                    dp[i][j]=true;
                }
            }
        }
        return dp[0][0];
    }
}
