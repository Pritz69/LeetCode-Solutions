class Solution {
    public boolean check(String s1,String s2)
    {
        if (s1.length() != s2.length()+1)
        {
            return false;
        }
        int l=0;
        int r=0;
        while (l<s1.length())
        {
            if (r<s2.length() && s1.charAt(l)==s2.charAt(r))
            {
                l +=1;
                r +=1;
            }
            else
            {
                l +=1;
            }
        }
        if (l==s1.length() && r==s2.length())
        {
            return true;
        }
        return false;
    }
    public int longestStrChain(String[] words) {
        Arrays.sort(words, (a,b)-> a.length()-b.length() );
        int n=words.length;
        int dp[]=new int[n];
        int m=1;
        for(int i=0;i<n;i++)
        {
            dp[i]=1;
            for(int j=0;j<i;j++)
            {
                if (check(words[i],words[j]) && (dp[j]+1) > dp[i])
                {
                    dp[i]=dp[j]+1;
                }
            }
            m=Math.max(m,dp[i]);
        }
        return m;
    }
}
