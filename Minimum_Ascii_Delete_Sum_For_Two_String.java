class Solution {
    public int lcs(String s1,String s2)
    {
        int n=s1.length();
        int m=s2.length();
        int dp[][]=new int[n+1][m+1];
        for(int i=1;i<=n;i++)
        {
            for(int j=1;j<=m;j++)
            {
                if (s1.charAt(i-1)==s2.charAt(j-1))
                {
                    int asc = s1.charAt(i-1);     
                    /*
                    Same as LCS, just in place of calculating the length of the longest subsequnce
                    (where we add 1, each time we find a common character), here
                    we are adding the ascii values of the characters present in the longest  subsequence.  
                    While determining the final ans, we add up the ascii values of both the strings and 
                    subtract twice the lcs ascii, to find the minimum ascii to be deleted. We subtract 
                    twice becoz its common in both the strings.
                    */
                    dp[i][j]= asc + dp[i-1][j-1];
                }
                else
                {
                    dp[i][j]= Math.max(dp[i-1][j],dp[i][j-1]);
                }
            }
        }
        return dp[n][m];
    }
    public int minimumDeleteSum(String s1, String s2) {
        int asc1=0;
        int asc2=0;
        for(int i=0;i<s1.length();i++)
        {
            int x=s1.charAt(i);
            asc1 += x;
        }
        for(int i=0;i<s2.length();i++)
        {
            int x=s2.charAt(i);
            asc2 +=x;
        }
        int comasc=lcs(s1,s2);
        int ans= asc1 + asc2 - (2*comasc);
        return ans;
    }
}
