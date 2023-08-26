class Solution {
    public int findLongestChain(int[][] pairs) {
        Arrays.sort(pairs, (a,b)-> a[1]-b[1]);
        int c=1;
        int st=pairs[0][1];
        for(int i=1;i<pairs.length;i++)
        {
            if(pairs[i][0]>st)
            {
                c +=1;
                st=pairs[i][1];
            }
        }
        return c;
    }
}
class Solution {
    public int findLongestChain(int[][] pairs) {
        Arrays.sort(pairs, (a,b)-> a[1]-b[1]);
        int dp[]=new int[pairs.length];
        int ma=Integer.MIN_VALUE;
        for(int i=0;i<pairs.length;i++)
        {
            dp[i]=1;
            for(int j=0;j<i;j++)
            {
                if(pairs[j][1]<pairs[i][0])
                {
                    dp[i]=Math.max(dp[i],dp[j]+1);
                }
            }
            ma=Math.max(ma,dp[i]);
        }
        return ma;
    }
}
