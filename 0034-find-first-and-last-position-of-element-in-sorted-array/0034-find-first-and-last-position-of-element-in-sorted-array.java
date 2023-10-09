class Solution {
    public int[] searchRange(int[] nums, int target) {
        int l=0;
        int r=nums.length-1;
        int lb=nums.length;
        int ub=nums.length;
        while (l<=r)
        {
            int m=(l+r)/2;
            if (nums[m]>=target)
            {
                lb=m;
                r=m-1;
            }
            else
            {
                l=m+1;
            }
        }
        l=0;
        r=nums.length-1;
        while (l<=r)
        {
            int m=(l+r)/2;
            if (nums[m]>target)
            {
                ub=m;
                r=m-1;
            }
            else
            {
                l=m+1;
            }
        }
        int a[]=new int[2];
        //System.out.println(lb+","+ub);
        if (lb==nums.length || nums[lb]!=target)
        {
            a[0]=-1;
            a[1]=-1;
            return a;
        }
        a[0]=lb;
        a[1]=ub-1;
        return a;
    }
}