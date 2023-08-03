class Solution {
    public void rotate(int[] arr, int k) {
        int n=arr.length;
        k=k%n;
        int l=0; int r=n-1;
        while (l<=r)
        {
            int t=arr[l];
            arr[l]=arr[r];
            arr[r]=t;                       //Rotate Enitre Array---Notice The Condition of array
            l +=1; r -=1;
        }
        l=0; r=k-1;
        while(l<=r)
        {
            int t=arr[l];
            arr[l]=arr[r];                  //sort upto k and its done!
            arr[r]=t;
            l +=1; r -=1;
        }
        l=k; r=n-1;
        while(l<=r)
        {
            int t=arr[l];
            arr[l]=arr[r];
            arr[r]=t;
            l +=1; r -=1;
        }
    }
}
/*  TLE SOLUTION
class Solution {
    public void rotate(int[] nums, int k) {
        if (k==0)
        {
            return ;
        }
        else
        {
            int p=1;
            int n=nums.length;
            while (p<=k)
            {
                int last=nums[n-1];
                for(int i=n-1;i>=1;i--)
                {
                    nums[i]=nums[i-1];
                }
                nums[0]=last;
                p +=1;
            }
        }
    }
}
*/
