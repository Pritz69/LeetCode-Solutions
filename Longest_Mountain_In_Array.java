class Solution {
    public int longestMountain(int[] arr) {
        int ans=0;
        int n=arr.length;
        for(int i=1;i<=n-2;)
        {
            if (arr[i]>arr[i-1] && arr[i]>arr[i+1])
            {
                int count=1;
                int j=i;
                while (j>0 && arr[j]>arr[j-1])
                {
                    count ++;
                    j --; 
                }
                while (i<n-1 && arr[i]>arr[i+1])
                {
                    count ++;
                    i ++;
                }
                ans=Math.max(ans,count);
            }
            else
            {
                i ++;
            }
        }
        return ans;
    }
}
