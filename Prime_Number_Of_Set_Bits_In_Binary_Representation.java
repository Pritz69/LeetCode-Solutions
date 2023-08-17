lass Solution {
    /*  public boolean isprime(int n)
        {
            if(n<=1)
            {
                return false;
            }
            for(int i=2;i<=(int)Math.sqrt(n);i++)
            {
                if(n%i==0)
                {
                    return false;
                }
            }
            return true;
        }
    */
    public int countPrimeSetBits(int left, int right) {
        int ans=0;
        Set<Integer> s=new HashSet<Integer>();
        int a[]={2,3,5,7,11,13,17,19,23,29,31,37};
        for(int x:a)
        {
            s.add(x);
        }
        for(int k=left;k<=right;k++)
        {
            int c=0;
            int i=k;
            while(i>0)
            {
                int v=i%2;
                if(v==1)
                {
                    c+=1;
                }
                i=i/2;
            }
            if(s.contains(c))
            {
                ans+=1;
            }
        }
        return ans;
    }
}
