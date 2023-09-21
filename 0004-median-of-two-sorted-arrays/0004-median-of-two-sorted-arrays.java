class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int n1=nums1.length;
        int n2=nums2.length;
        if (n1>n2)
        {
            return findMedianSortedArrays(nums2,nums1);
        }
        int n=n1+n2;
        int low=0;
        int high=n1;
        int left=(n1+n2+1)/2;
        while(low<=high)
        {
            int mid1=(low+high)/2;
            int mid2=left-mid1;
            int l1=Integer.MIN_VALUE;
            int l2=Integer.MIN_VALUE;
            int r1=Integer.MAX_VALUE;
            int r2=Integer.MAX_VALUE;
            if (mid1 < n1)
            {
                r1=nums1[mid1];
            }
            if (mid2 < n2)
            {
                r2=nums2[mid2];
            }
            if (mid1-1 >=0)
            {
                l1=nums1[mid1-1];
            }
            if (mid2-1 >=0)
            {
                l2=nums2[mid2-1];
            }
            if(l1<=r2 && l2<=r1)
            {
                if(n%2==1)
                {
                    return Math.max(l1,l2);
                }
                else
                {
                    return (double)((Math.max(l1,l2)+ Math.min(r1,r2))/2.0) ;
                }
            }
            if(l2>r1)
            {
                low=mid1+1;
            }
            if(l1>r2)
            {
                high=mid1-1;
            }
        }
        return 0;
    }
}