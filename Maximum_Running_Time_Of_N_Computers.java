class Solution {
    public boolean check(long t,int n,int batteries[])
    {
        long s=0;
        for(long x:batteries)
        {
            s += Math.min(t,x);
        }
        long need=t*n;
        return s>=need;
    }
    public long maxRunTime(int n, int[] batteries) {
        long s=0;
        for(long x:batteries)
        {
            s+=x;
        }
        long l=1;
        long r=s/n;
        long ans=1;
        while (l<=r)
        {
            long m=(l+r)/2;
            if (check(m,n,batteries))
            {
                ans=m;
                l=m+1;
            }
            else
            {
                r=m-1;
            }
        }
        return ans;
    }
}
