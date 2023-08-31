class Solution {
    public int minTaps(int n, int[] ranges) {
        int rmax[]=new int[n+1];
        int lp;
        for(int i=0;i<=n;i++)
        {
            lp=Math.max(i-ranges[i],0);
            rmax[lp]=Math.max(rmax[lp],i+ranges[i]);
        }
        /*for(int i=0;i<=n;i++)
        {
            System.out.print(rmax[i]);
        }*/
        int c=0;
        int l=0;
        int r=0;
        int f;
        while(r<n)
        {
            f=0;
            for(int i=l;i<=r;i++)
            {
                f=Math.max(f,rmax[i]);
            }
            l=r+1;
            r=f;                            // Implementation Of Jump Game II 
            if(l>r)                        
            {
                return -1;                  // Not possible scenario.
            }
            c +=1;
        }
        return c;
    }
}
