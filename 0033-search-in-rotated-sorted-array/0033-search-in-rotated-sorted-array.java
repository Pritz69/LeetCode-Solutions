class Solution {
    public int search(int[] arr, int target) {
        int l=0;
        int r=arr.length-1;
        while (l<=r)
        {
            int m=(l+r)/2;
            if (arr[m]==target)
            {
                return m;
            }
            if(arr[l]<=arr[m] )
            {
                if (arr[l]<=target && target<=arr[m])
                {
                    r=m-1;
                }
                else
                {
                    l=m+1;
                }     
            }
            else
            {
                if(arr[m]<=target && target<=arr[r])
                {
                    l=m+1;
                }
                else
                {
                    r=m-1;
                }
            }
        }
        return -1;
    }
}