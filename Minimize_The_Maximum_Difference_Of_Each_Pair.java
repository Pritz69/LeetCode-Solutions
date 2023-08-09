class Solution {
    public boolean check(int nums[],int p,int m)
    {
        int i=0;
        int j=1;
        int c=0;
        while (j<nums.length)
        {
            if(nums[j]-nums[i]<=m)
            {
                c +=1;      // +1 for each pair formed by i and j
                i +=2;                    
                j +=2;   
            }                  // 1 1 2 3 7 9 10 , p=3
            else
            {
                i +=1;
                j +=1;      // moving to the next pair---
            }
        }
        return c >= p ;
    }
    public int minimizeMax(int[] nums, int p) {
        Arrays.sort(nums);
        int r=nums[nums.length-1]-nums[0];
        int l=0;
        int ans=-1;
        while (l<=r)
        {
            int m=(l+r)/2;
            if (check(nums,p,m))
            {
                ans=m;
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
