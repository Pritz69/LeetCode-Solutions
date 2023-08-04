class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        int n=s.length();
        int dp[]=new int[n+1];
        dp[n]=1;
        for(int i=n-1;i>=0;i--)
        {
            for(String w:wordDict)
            {
                if(i+w.length()<=n && s.substring(i,i+w.length()).equals(w))
                {
                    dp[i]=dp[i+w.length()];
                }
                if (dp[i]==1)
                {
                    break;
                }
            }
        }
        if (dp[0]==1)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
}
