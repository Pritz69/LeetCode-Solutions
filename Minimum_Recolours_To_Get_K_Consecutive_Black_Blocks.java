class Solution {
    public int minimumRecolors(String blocks, int k) {
        int ans=Integer.MAX_VALUE;
        int n=blocks.length();
        int l=0;
        int r=0;
        int c=0;
        while(r<n)
        {
            if(blocks.charAt(r)=='W')
            {
                c+=1;
            }
            if((r-l+1)==k)
            {
                ans=Math.min(ans,c);
                if(blocks.charAt(l)=='W')
                {
                    c -=1;
                }
                l +=1;
            }
            r +=1;
        }
        return ans;
    }
}

class Solution {
    public int minimumRecolors(String blocks, int k) {
        int ans=Integer.MAX_VALUE;
        int n=blocks.length();
        int c=0;
        for(int i=0;i<=n-k;i++)
        {
            c=0;
            for(int j=i;j<(i+k);j++)
            {
                if(blocks.charAt(j)=='W')
                {
                    c +=1;
                }
            }
            ans=Math.min(ans,c);
        }
        return ans;
    }
}
