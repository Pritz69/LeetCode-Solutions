class Solution {
    public int peakIndexInMountainArray(int[] arr) {
        int n=arr.length;
        if(arr[0]>arr[1])
        {
            return 0;
        }
        if(arr[n-1]>arr[n-2])
        {
            return n-1;
        }
        int l=1;
        int r=n-2;
        while (l<=r)
        {
            int m=(l+r)/2;
            if(arr[m]>arr[m-1] && arr[m]>arr[m+1])
            {
                return m;
            }
            if (arr[m]>arr[m-1])
            {
                l=m+1;
            }
            else if(arr[m]>arr[m+1])
            {
                r=m-1;
            }
        }
        return 0;
    }
}
