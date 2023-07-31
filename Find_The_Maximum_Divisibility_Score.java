class Solution {
    public int maxDivScore(int[] nums, int[] divisors) {
        Arrays.sort(divisors);
        int max=Integer.MIN_VALUE;
        int maxel=Integer.MIN_VALUE;
        int minel=Integer.MAX_VALUE;
        int f=0;
        int a[]=new int[divisors.length];
        for(int i=0;i<divisors.length;i++)
        {
            int c=0;
            for(int j=0;j<nums.length;j++)
            {
                if(nums[j]%divisors[i]==0)
                {
                    c +=1;
                }
            }
            max=Math.max(max,c);
            a[i]=c;
        }
        for(int i=0;i<a.length;i++)
        {
            if (a[i]==max)
            {
                f +=1;
                maxel=Math.max(maxel,divisors[i]);
                minel=Math.min(minel,divisors[i]);
            }
        }
        if (f>1)
        {
            return minel;
        }
        else
        {
            return maxel;
        }
    }
}
