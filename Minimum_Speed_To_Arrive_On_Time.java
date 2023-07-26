class Solution {
    public boolean time(int dist[],double t,double hour)
    {
        double s=0;
        for(int i=0;i<dist.length;i++)
        {
            if(i !=dist.length-1)
            {
                double ti=Math.ceil(dist[i]/t*1.0);
                s +=ti;
            }
            else
            {
                double ti=dist[i]/t*1.0;
                s +=ti;
            }
        }
        if(s<=hour)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
    public int minSpeedOnTime(int[] dist, double hour) {
        int l=0;
        int r=10000000;
        int ans=-1;
        while (l<=r)
        {
            int m=(l+r)/2;
            if (time(dist,m,hour))
            {
                ans=(int)m;
                r=m-1;
            }
            else
            {
                l=m+1;
            }
        }
        return ans;
    }
}
